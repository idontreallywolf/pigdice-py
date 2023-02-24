"""Test class."""
import unittest
from src.config import CHOICE_HOLD, CHOICE_ROLL
from src.player import Player
from src.ai_player import AIPlayer


class TestAIplayer(unittest.TestCase):
    """Do test."""

    def setUp(self):
        """Set up."""
        self.player = AIPlayer()

    def tearDown(self):
        """Tear down."""
        pass

    def test_make_choice_1(self):
        """Test the value of return of this function."""
        expected = CHOICE_HOLD
        result = self.player.make_choice(7, 15)
        self.assertEqual(expected, result)

    def test_make_choice_2(self):
        """Test the value of return of this function."""
        expected = CHOICE_HOLD
        result = self.player.make_choice(15, 6)
        self.assertEqual(expected, result)

    def test_make_choice_3(self):
        """Test the value of return of this function."""
        expected = CHOICE_ROLL
        result = self.player.make_choice(36, 72)
        self.assertEqual(expected, result)

    def test_make_choice_4(self):
        """Test the value of return of this function."""
        expected = CHOICE_ROLL
        result = self.player.make_choice(72, 24)
        self.assertEqual(expected, result)

    def test_get_expected_score_1(self):
        """Test the value of return of this function with turn score 0."""
        expected = 3.5
        result = self.player._get_expected_score(0)
        self.assertEqual(expected, result)

    def test_get_expected_score_2(self):
        """Test the value of return of this function."""
        expected = 8.5
        result = self.player._get_expected_score(5)
        self.assertEqual(expected, result)

    def test_get_expected_score_3(self):
        """Test the value of return of this function."""
        expected = 13.499999999999998
        result = self.player._get_expected_score(10)
        self.assertEqual(expected, result)

    def test_get_expected_score_returns_float(self):
        """Test if _get_expected_score returns float value."""
        turn_score = 3
        expected_scord = self.player._get_expected_score(turn_score)
        self.assertIsInstance(expected_scord, float)

    def test_player_name_is_set_properly(self):
        """Test if Player name is set properly in constructor."""
        AIPlayer = self.player.get_name()
        self.assertEquals(AIPlayer, 'AI')

    def test_threshold_initialized_properly(self):
        """Test if threshold is initialized properly in constructor."""
        self.assertEquals(self.player.threshold, 20)


if __name__ == '__main__':
    unittest.main()
