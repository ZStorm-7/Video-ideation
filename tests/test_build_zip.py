"""Guards the Claude-app install file: limits on name/description and the ZIP layout. Offline."""
import os, sys, tempfile, unittest, zipfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
import build_zip, yt  # noqa: E402


class SkillFile(unittest.TestCase):
    def test_description_fits_the_claude_app_limit(self):
        # The Claude app rejects descriptions over 200 characters, so a long edit here would break the one-click install.
        name, desc = build_zip.frontmatter(os.path.join(yt.ROOT, 'SKILL.md'))
        self.assertEqual(name, 'idea-scout')
        self.assertLessEqual(len(desc), build_zip.MAX_DESC, len(desc))
        self.assertEqual(build_zip.problems()[1], [])

    def test_frontmatter_is_valid_yaml_if_pyyaml_is_installed(self):
        try: import yaml
        except ImportError: self.skipTest('pyyaml not installed')
        with open(os.path.join(yt.ROOT, 'SKILL.md'), encoding='utf-8') as f: fm = f.read().split('---')[1]
        self.assertEqual(set(yaml.safe_load(fm)), {'name', 'description'})


class Zip(unittest.TestCase):
    def test_layout(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, 'idea-scout.zip'); build_zip.build(out)
            names = zipfile.ZipFile(out).namelist()
        self.assertIn('idea-scout/SKILL.md', names)
        self.assertTrue(all(n.startswith('idea-scout/') for n in names), 'every file must sit inside the skill folder')
        for needed in ('workflow/00-start.md', 'tools/notes.py', 'library/hooks.md', 'niches/_template.md', 'templates/creator-profile.md'):
            self.assertIn('idea-scout/' + needed, names)
        for unwanted in ('tests/', '.github/', 'CONTRIBUTING.md', '__pycache__'):
            self.assertFalse(any(unwanted in n for n in names), unwanted)

    def test_refuses_an_overlong_description(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, 'x'))
            with open(os.path.join(d, 'SKILL.md'), 'w') as f: f.write('---\nname: idea-scout\ndescription: ' + 'x' * 201 + '\n---\n')
            self.assertTrue(build_zip.problems(d)[1])

    def test_refuses_a_description_that_breaks_yaml(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, 'SKILL.md'), 'w') as f: f.write('---\nname: idea-scout\ndescription: Built from proof: finds videos\n---\n')
            self.assertTrue(any('YAML' in e for e in build_zip.problems(d)[1]))


if __name__ == '__main__':
    unittest.main()
