"""Guards the docs that make the skill easy to get and trustworthy: install paths, copy-paste prompts, saved recap, why-it-worked."""
import os, re, subprocess, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFFICIAL = 'https://github.com/ZStorm-7/Video-ideation'


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f: return f.read()


def markdown_files():
    tracked = subprocess.check_output(['git', '-C', ROOT, 'ls-files', '-co', '--exclude-standard'], text=True).split('\n')
    return [f for f in tracked if f.endswith('.md') and not f.startswith(('examples/', '.github/'))]


class CopyPastePrompts(unittest.TestCase):
    def lite(self):
        m = re.search(r'````\n(.*?)\n````', read('prompts/idea-scout-lite.md'), re.S)
        self.assertIsNotNone(m, 'the prompt must sit inside a four-backtick block')
        return m.group(1)

    def test_lite_prompt_is_self_contained(self):
        p = self.lite()
        for repo_thing in ('workflow/', 'library/', 'niches/', 'templates/', 'tools/', 'SKILL.md', '<notes>', 'notes.py'):
            self.assertNotIn(repo_thing, p, f'the pasted prompt cannot point at repo files ({repo_thing})')
        self.assertLess(len(p), 14000, 'keep it short enough to paste anywhere')

    def test_lite_prompt_has_every_step_and_the_honesty_rules(self):
        p = self.lite()
        flat = ' '.join(p.split()).lower()  # the prompt is line-wrapped
        for i in range(8): self.assertIn(f'STEP {i}', p)
        for must in ('Never invent data', 'unverified', 'Observed', 'Hypothesis', 'Saved', 'idea-scout-notes', 'Never put passwords'):
            self.assertIn(must.lower(), flat, must)

    def test_lite_prompt_blocks_invented_observations_and_rule_bending(self):
        flat = ' '.join(self.lite().split()).lower()
        for must in ('not seen', 'rule check', 'every candidate', 'fail', 'never talk yourself into an exception', 'never re-ask', 'channel name', 'always low', 'either ratio is 10 or more', 'known:', 'missing:', 'build the table first', 'under 10,000 subscribers', 'never write my replies for me', 'saved ·', 'unverified guess', 'plain sum', 'unverified trend', 'do only that', 'a reply without the notes block is incomplete', 'i have no benchmark', 'finish like step 7', 'this is result n', 'backlog status:', 'never quote a', 'do the request first'):
            self.assertIn(must, flat, must)

    def test_loader_points_at_the_raw_skill_file(self):
        self.assertIn('https://raw.githubusercontent.com/ZStorm-7/Video-ideation/main/SKILL.md', read('prompts/idea-scout-loader.md'))


class InstallForAgents(unittest.TestCase):
    def test_install_md_only_uses_the_official_repo_and_nothing_risky(self):
        t = read('INSTALL.md')
        for clone in re.findall(r'git clone (\S+)', t): self.assertEqual(clone, OFFICIAL)
        for risky in ('curl ', 'wget ', '| sh', '| bash', 'sudo ', 'chmod'):
            self.assertNotIn(risky, t, risky)

    def test_readme_offers_all_three_options(self):
        t = read('README.md')
        for needed in ('Option 1', 'Option 2', 'Option 3', 'idea-scout.zip', 'git clone', 'INSTALL.md', 'idea-scout-lite.md', 'idea-scout-loader.md'):
            self.assertIn(needed, t, needed)


class Features(unittest.TestCase):
    def test_save_recap_is_documented_and_templated(self):
        self.assertIn('## Saving', read('SKILL.md'))
        self.assertIn('## Saved', read('templates/ideas-output.md'))
        self.assertIn('Saved', read('workflow/07-deliver-and-remember.md'))

    def test_outliers_explain_why_and_label_evidence(self):
        for rel in ('workflow/03-find-outliers.md', 'templates/outliers.md'):
            t = read(rel)
            self.assertIn('Observed', t, rel); self.assertIn('Hypothesis', t, rel)
        self.assertIn('Confidence', read('workflow/03-find-outliers.md'))
        for rel in ('workflow/03-find-outliers.md', 'templates/outliers.md', 'SKILL.md'):
            self.assertIn('not seen', read(rel), rel)


class Links(unittest.TestCase):
    def test_referenced_repo_files_exist(self):
        path_re = re.compile(r'`((?:workflow|library|niches|templates|tools|docs|prompts|examples|tests)/[\w./-]+\.(?:md|py)|[A-Z]+\.md)`')
        link_re = re.compile(r'\]\(([^)#\s]+)\)')
        broken = []
        for f in markdown_files():
            text, base = read(f), os.path.dirname(f)
            for ref in path_re.findall(text):
                if not os.path.exists(os.path.join(ROOT, ref)): broken.append((f, ref))
            for ref in link_re.findall(text):
                if ref.startswith(('http', 'mailto:')) or f.startswith('templates/'): continue  # templates hold placeholder links
                if not os.path.exists(os.path.join(ROOT, base, ref)): broken.append((f, ref))
        self.assertEqual(broken, [])


if __name__ == '__main__':
    unittest.main()
