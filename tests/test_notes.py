"""Offline tests for tools/notes.py (the private notes repo helper). Uses temp folders and a local bare git repo."""
import contextlib, io, os, subprocess, sys, tempfile, unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
import notes, yt  # noqa: E402

GIT_ENV = dict(GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@example.com', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@example.com')


class Args:
    def __init__(self, **kw): self.__dict__.update(kw)


class NotesCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.path = os.path.join(self.tmp.name, 'my-notes')
        patch = mock.patch.dict(os.environ, {'IDEA_SCOUT_NOTES': self.path, **GIT_ENV}); patch.start(); self.addCleanup(patch.stop)

    def run_cmd(self, fn, **kw):
        out = io.StringIO()
        with contextlib.redirect_stdout(out): rc = fn(Args(**kw))
        return rc, out.getvalue()

    def init(self):
        return self.run_cmd(notes.cmd_init, path=None, import_from=None)


class Location(NotesCase):
    def test_env_var_wins(self):
        self.assertEqual(yt.notes_dir(), os.path.abspath(self.path))

    def test_default_is_home_folder(self):
        with mock.patch.dict(os.environ, {'IDEA_SCOUT_NOTES': ''}):
            self.assertEqual(yt.notes_dir(), os.path.expanduser('~/idea-scout-notes'))


class Init(NotesCase):
    def test_creates_templates_gitignore_and_repo(self):
        self.init()
        for f in ('profile.md', 'past-videos.md', 'outliers.md', 'backlog.md', 'feedback.md', 'session-log.md', 'README.md', '.gitignore'):
            self.assertTrue(os.path.exists(os.path.join(self.path, f)), f)
        self.assertTrue(os.path.isdir(os.path.join(self.path, '.git')))

    def test_does_not_overwrite_existing_notes(self):
        self.init()
        with open(os.path.join(self.path, 'profile.md'), 'w') as f: f.write('my real profile')
        self.init()
        with open(os.path.join(self.path, 'profile.md')) as f: self.assertEqual(f.read(), 'my real profile')

    def test_import_from_legacy_creator_folder(self):
        old = os.path.join(self.tmp.name, 'creator'); os.makedirs(old)
        with open(os.path.join(old, 'profile.md'), 'w') as f: f.write('legacy profile')
        self.run_cmd(notes.cmd_init, path=None, import_from=old)
        with open(os.path.join(self.path, 'profile.md')) as f: self.assertEqual(f.read(), 'legacy profile')


class Safety(NotesCase):
    def test_github_url_parsing(self):
        self.assertEqual(notes.github_repo('https://github.com/me/idea-scout-notes.git'), ('me', 'idea-scout-notes'))
        self.assertEqual(notes.github_repo('git@github.com:me/idea-scout-notes.git'), ('me', 'idea-scout-notes'))
        self.assertIsNone(notes.github_repo('/some/local/path'))

    def test_secrets_are_found_but_never_printed(self):
        self.init()
        fake = 'AIza' + 'x' * 35
        with open(os.path.join(self.path, 'profile.md'), 'a') as f: f.write(f'my key is {fake}\n')
        with open(os.path.join(self.path, 'x.env'), 'w') as f: f.write('A=b\n')
        found = notes.find_secrets(self.path)
        self.assertIn(('profile.md', 'Google/YouTube API key'), found)
        self.assertIn(('x.env', 'env file'), found)
        self.assertNotIn(fake, str(found))

    def test_clean_notes_have_no_secrets(self):
        self.init(); self.assertEqual(notes.find_secrets(self.path), [])

    def test_public_remote_is_an_error(self):
        self.init(); subprocess.run(['git', '-C', self.path, 'remote', 'add', 'origin', 'https://github.com/me/notes.git'], check=True)
        with mock.patch.object(notes, 'is_public', return_value=True):
            errs, _ = notes.problems(self.path)
        self.assertTrue(any('PUBLIC' in e for e in errs))

    def test_private_remote_passes_and_unknown_warns(self):
        self.init(); subprocess.run(['git', '-C', self.path, 'remote', 'add', 'origin', 'https://github.com/me/notes.git'], check=True)
        with mock.patch.object(notes, 'is_public', return_value=False): self.assertEqual(notes.problems(self.path), ([], []))
        with mock.patch.object(notes, 'is_public', return_value=None):
            errs, warns = notes.problems(self.path)
        self.assertEqual(errs, []); self.assertTrue(warns)

    def test_notes_inside_the_skill_repo_are_refused(self):
        inside = os.path.join(yt.ROOT, 'tmp-notes-test'); os.makedirs(os.path.join(inside, '.git'))
        self.addCleanup(lambda: __import__('shutil').rmtree(inside, ignore_errors=True))
        errs, _ = notes.problems(inside)
        self.assertTrue(any('inside the public skill repo' in e for e in errs))


class PublicCheck(unittest.TestCase):
    """is_public must not let a rate-limited or unclear GitHub API answer slip through as 'fine'."""
    def raises(self, code):
        err = urllib_error(code); self.addCleanup(err.close)  # an HTTPError holds a file: close it or newer Pythons warn
        return err

    def test_404_means_not_public(self):
        with mock.patch('urllib.request.urlopen', side_effect=self.raises(404)):
            self.assertIs(notes.is_public('o', 'r'), False)

    def test_rate_limited_api_falls_back_to_anonymous_git(self):
        with mock.patch('urllib.request.urlopen', side_effect=self.raises(403)), mock.patch.object(notes, 'public_via_git', return_value=True) as g:
            self.assertIs(notes.is_public('o', 'r'), True); g.assert_called_once()

    def test_git_fallback_reads_the_error(self):
        def run(rc, err): return mock.Mock(returncode=rc, stderr=err)
        with mock.patch('subprocess.run', return_value=run(0, '')): self.assertIs(notes.public_via_git('o', 'r'), True)
        with mock.patch('subprocess.run', return_value=run(128, "fatal: could not read Username for 'https://github.com'")): self.assertIs(notes.public_via_git('o', 'r'), False)
        with mock.patch('subprocess.run', return_value=run(128, 'fatal: unable to access: Could not resolve host: github.com')): self.assertIsNone(notes.public_via_git('o', 'r'))

    def test_git_fallback_ignores_stored_credentials(self):
        with mock.patch('subprocess.run', return_value=mock.Mock(returncode=0, stderr='')) as run:
            notes.public_via_git('o', 'r')
        cmd = run.call_args[0][0]
        self.assertIn('credential.helper=', cmd)  # an empty helper: a private repo must not look public because we are logged in
        self.assertEqual(run.call_args[1]['env']['GIT_TERMINAL_PROMPT'], '0')


def urllib_error(code):
    import urllib.error
    return urllib.error.HTTPError('https://api.github.com/x', code, 'x', {}, __import__('io').BytesIO(b''))


class Save(NotesCase):
    def test_save_commits_and_pushes_to_a_remote(self):
        self.init()
        bare = os.path.join(self.tmp.name, 'remote.git'); subprocess.run(['git', 'init', '-q', '--bare', bare], check=True)
        subprocess.run(['git', '-C', self.path, 'remote', 'add', 'origin', bare], check=True)
        rc, out = self.run_cmd(notes.cmd_save, message='first notes')
        self.assertEqual(rc, 0, out)
        # --all: the bare repo's own HEAD may point at "master" while we push "main"
        log = subprocess.run(['git', '-C', bare, 'log', '--all', '--oneline'], capture_output=True, text=True).stdout
        self.assertIn('idea-scout: first notes', log)

    def test_save_refuses_when_a_key_is_present(self):
        self.init()
        with open(os.path.join(self.path, 'session-log.md'), 'a') as f: f.write('YT_API_KEY=abcdefghijklmnop\n')
        rc, out = self.run_cmd(notes.cmd_save, message='oops')
        self.assertEqual(rc, 1); self.assertIn('not saved', out)
        self.assertEqual(subprocess.run(['git', '-C', self.path, 'log', '--oneline'], capture_output=True, text=True).stdout.strip(), '')


if __name__ == '__main__':
    unittest.main()
