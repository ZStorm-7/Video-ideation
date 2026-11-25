"""Offline tests for the tools (no network, no API key). Run from the repo root:  python3 -m unittest discover -s tests"""
import os, sys, tempfile, unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
import overlap, yt  # noqa: E402


class Words(unittest.TestCase):
    def sim(self, a, b):
        wa, wb = overlap.words(a), overlap.words(b)
        return max(len(wa & wb) / max(1, len(wa)), len(wa & wb) / max(1, len(wb)))

    def test_english_hyphens_and_stemming(self):
        self.assertEqual(overlap.words("Why your Wi-Fi is slower upstairs"), {'wifi', 'slower', 'upstair'})

    def test_accents_stay_in_the_word(self):
        # Regression: "móvil" used to be split into "m" + "vil".
        self.assertIn('móvil', overlap.words("¿Por qué tu móvil carga más lento?"))

    def test_hindi_is_not_empty(self):
        # Regression: non-Latin titles produced an empty set, so every idea passed the repeat check.
        self.assertTrue(overlap.words("तुम्हारा फोन धीमा क्यों चार्ज होता है"))
        self.assertIn('फोन', overlap.words("तुम्हारा फोन धीमा क्यों चार्ज होता है"))

    def test_chinese_uses_character_pairs(self):
        self.assertTrue(overlap.words("为什么手机充电越来越慢"))
        self.assertGreater(self.sim("为什么手机充电越来越慢", "手机充电为什么越来越慢"), 0.5)

    def test_repeat_detected_in_other_languages(self):
        self.assertGreaterEqual(self.sim("Por qué tu móvil carga lento", "Por qué tu móvil carga más lento después del 80%"), 0.5)
        self.assertGreaterEqual(self.sim("तुम्हारा फोन धीमा क्यों चार्ज होता है", "फोन धीमा चार्ज क्यों होता है"), 0.5)

    def test_different_topics_are_not_flagged(self):
        self.assertLess(self.sim("Why your Wi-Fi is slower upstairs", "How to cook perfect rice"), 0.5)
        self.assertLess(self.sim("¿Por qué tu móvil carga más lento?", "Cómo cocinar arroz perfecto"), 0.5)


class Titles(unittest.TestCase):
    def read(self, text):
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(text)
        self.addCleanup(os.unlink, f.name)
        return overlap.titles(f.name)

    def test_past_videos_table(self):
        md = ("# Past videos\nUpdated: 2026-11-24\n\n| Date | Format | Title | Views | vs median | Flag | Link |\n|---|---|---|---|---|---|---|\n"
              "| 2026-11-20 | short | 2038 Bug: Your Computer Will Think It's 1901 | 1,685 | 1.3x | | https://youtube.com/shorts/x |\n")
        self.assertEqual(self.read(md), ["2038 Bug: Your Computer Will Think It's 1901"])

    def test_outliers_table_with_links(self):
        md = ("| Found | Format | Title + link | Channel | Subs | Views | Channel avg | Ratio | Niche |\n|---|---|---|---|---|---|---|---|---|\n"
              "| 2026-11-24 | short | [Why Apple Store iPhones Don't Have Security Cables](https://youtube.com/shorts/abc) | Some Channel | 12,700 | 704,731 | 10,000 | 55x / 70x | tech |\n")
        self.assertEqual(self.read(md), ["Why Apple Store iPhones Don't Have Security Cables"])

    def test_missing_file(self):
        self.assertEqual(overlap.titles('/nonexistent/file.md'), [])


class Helpers(unittest.TestCase):
    def test_iso_duration(self):
        self.assertEqual(yt.iso_dur('PT45S'), 45)
        self.assertEqual(yt.iso_dur('PT1M30S'), 90)
        self.assertEqual(yt.iso_dur('PT1H2M3S'), 3723)
        self.assertEqual(yt.iso_dur(''), 0)

    def test_median(self):
        self.assertEqual(yt.median([]), 0)
        self.assertEqual(yt.median([1, 9, 5]), 5)


if __name__ == '__main__':
    unittest.main()
