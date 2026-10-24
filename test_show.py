import unittest

from show import LETTERS, perform_custom, segments_for
from show import ScriptError


class ShowTests(unittest.TestCase):
    def test_series_is_six_two_act_letters(self):
        ids = [letter["id"] for letter in LETTERS]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(LETTERS), 6)
        for letter in LETTERS:
            scenes = segments_for(letter)
            self.assertEqual(len(scenes), 3)
            joined = " ".join(line["text"] for scene in scenes for line in scene["lines"])
            self.assertGreater(len(joined), 1200)
            for scene in scenes:
                self.assertLess(len(scene["text"].encode()), 4500)
                self.assertGreaterEqual(scene["text"].count("<|speaker:"), 2)
                self.assertEqual(len(scene["voice_ids"]), len(set(scene["voice_ids"])))
                self.assertNotIn("[", " ".join(line["text"] for line in scene["lines"]))

    def test_custom_letter_strips_direction_marks(self):
        scene = perform_custom(
            "Dev [angry]",
            "<|speaker:0|> <whisper>I am leaving the sentence out.</whisper>",
            "sheila",
        )
        spoken = " ".join(line["text"] for line in scene["lines"])
        self.assertIn("I am leaving the sentence out.", spoken)
        self.assertNotIn("whisper", spoken)
        self.assertNotIn("[", spoken)
        self.assertEqual(scene["text"].count("<|speaker:"), 3)

    def test_custom_rejects_blank_and_unknown_voice(self):
        with self.assertRaises(ScriptError):
            perform_custom("June", "   [pause]  ", "adrian")
        with self.assertRaises(ScriptError):
            perform_custom("June", "Come home.", "delia")


if __name__ == "__main__":
    unittest.main()
