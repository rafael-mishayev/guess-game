import unittest
from unittest.mock import patch

from number_game import play_number_game
from word_game import play_word_game, _render


class NumberGameTests(unittest.TestCase):
    @patch("number_game.random.randint", return_value=42)
    @patch("builtins.input", side_effect=["42"])
    def test_correct_guess_wins(self, mock_input, mock_randint):
        self.assertTrue(play_number_game())

    @patch("number_game.random.randint", return_value=1)
    @patch("builtins.input", side_effect=["100"] * 7)
    def test_running_out_of_attempts_loses(self, mock_input, mock_randint):
        self.assertFalse(play_number_game())

    @patch("number_game.random.randint", return_value=5)
    @patch("builtins.input", side_effect=["abc", "5"])
    def test_invalid_input_is_reprompted(self, mock_input, mock_randint):
        self.assertTrue(play_number_game())


class WordGameTests(unittest.TestCase):
    def test_render_shows_only_guessed_letters(self):
        self.assertEqual(_render("cat", {"c", "t"}), "c _ t")

    @patch("word_game.random.choice", return_value="cat")
    @patch("builtins.input", side_effect=["c", "a", "t"])
    def test_full_word_guessed_wins(self, mock_input, mock_choice):
        self.assertTrue(play_word_game())

    @patch("word_game.random.choice", return_value="cat")
    @patch("builtins.input", side_effect=["x", "y", "z", "q", "w", "e"])
    def test_running_out_of_guesses_loses(self, mock_input, mock_choice):
        self.assertFalse(play_word_game())


if __name__ == "__main__":
    unittest.main()
