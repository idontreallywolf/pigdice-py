"""Test dice class."""
import unittest

from src.dice import Dice


class TestDice(unittest.TestCase):
    """Creat TestDice calss."""

    def setUp(self):
        """Dice object."""
        self.dice = Dice()

    def test_roll_amount(self):
        """Test all of the rolls are within range."""
        rolls = self.dice.roll(5)
        for roll in rolls:
            self.assertTrue(
                1 <= roll <= self.dice.num_sides,
                f'Roll {roll} is out of range'
            )

    def test_roll_single(self):
        """Test value type and valid value."""
        result = self.dice.roll()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, self.dice.num_sides)
        self.assertTrue(1 <= result <= 6)

    def test_roll_multiple(self):
        """Test tuple."""
        count = 4
        result = self.dice.roll(count)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), count)
        for value in result:
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, self.dice.num_sides)

    def test_exceptions(self):
        """Test input is not an integer."""
        with self.assertRaises(TypeError):
            self.dice.roll("Invalid")
        with self.assertRaises(TypeError):
            self.dice.roll(5.5)
        with self.assertRaises(TypeError):
            self.dice.roll([1,2,3])

    def test_intialization(self):
        """Test that the object initializes properly."""
        self.assertIsInstance(self.dice, Dice)

    def test_str(self):
        """Test that str representation works."""
        self.assertEqual(str(self.dice), "Dice with 6 sides")


if __name__ == '__main__':
    unittest.main()
