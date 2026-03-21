"""
Unit Tests for Number Guessing Game
=====================================
Tests cover the core logic functions: random number generation,
hint generation, and input validation.
"""

import unittest
from unittest.mock import patch
from game import get_random_number, get_hint, get_player_guess


class TestGetRandomNumber(unittest.TestCase):
    """Tests for the get_random_number function."""

    def test_default_range(self):
        """Number should be between 1 and 100 by default."""
        number = get_random_number()
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 100)

    def test_custom_range(self):
        """Number should be within a custom range."""
        number = get_random_number(50, 60)
        self.assertGreaterEqual(number, 50)
        self.assertLessEqual(number, 60)

    def test_single_value_range(self):
        """When low equals high, the result should always be that value."""
        number = get_random_number(42, 42)
        self.assertEqual(number, 42)

    def test_returns_integer(self):
        """Result should always be an integer."""
        self.assertIsInstance(get_random_number(), int)


class TestGetHint(unittest.TestCase):
    """Tests for the get_hint function."""

    def test_guess_too_low(self):
        """Should return 'Too low!' when the guess is below the secret."""
        self.assertEqual(get_hint(30, 50), "Too low!")

    def test_guess_too_high(self):
        """Should return 'Too high!' when the guess is above the secret."""
        self.assertEqual(get_hint(80, 50), "Too high!")

    def test_guess_correct(self):
        """Should return 'Correct!' when the guess matches the secret."""
        self.assertEqual(get_hint(50, 50), "Correct!")

    def test_boundary_one_below(self):
        """One below the secret should still return 'Too low!'."""
        self.assertEqual(get_hint(49, 50), "Too low!")

    def test_boundary_one_above(self):
        """One above the secret should still return 'Too high!'."""
        self.assertEqual(get_hint(51, 50), "Too high!")


class TestGetPlayerGuess(unittest.TestCase):
    """Tests for the get_player_guess function."""

    @patch("builtins.input", return_value="50")
    def test_valid_input(self, mock_input):
        """Valid input within range should be returned as an integer."""
        result = get_player_guess(1, 100)
        self.assertEqual(result, 50)

    @patch("builtins.input", side_effect=["abc", "50"])
    def test_invalid_then_valid_input(self, mock_input):
        """Non-integer input should be rejected; next valid input is returned."""
        result = get_player_guess(1, 100)
        self.assertEqual(result, 50)

    @patch("builtins.input", side_effect=["0", "101", "55"])
    def test_out_of_range_then_valid(self, mock_input):
        """Out-of-range inputs should be rejected until a valid guess is given."""
        result = get_player_guess(1, 100)
        self.assertEqual(result, 55)

    @patch("builtins.input", return_value="1")
    def test_lower_boundary(self, mock_input):
        """The lower boundary value should be accepted."""
        result = get_player_guess(1, 100)
        self.assertEqual(result, 1)

    @patch("builtins.input", return_value="100")
    def test_upper_boundary(self, mock_input):
        """The upper boundary value should be accepted."""
        result = get_player_guess(1, 100)
        self.assertEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
