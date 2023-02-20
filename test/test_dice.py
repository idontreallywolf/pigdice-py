import unittest
import random
from src.dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll_amount(self):
        rolls = self.dice.roll(5)
        for roll in rolls:
            self.assertTrue(1 <= roll <= 6, f'Roll {roll} is out of range')

    def test_roll_single(self):
        result = self.dice.roll()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, self.dice.num_sides)
        self.assertTrue(1 <= result <= 6)

        
    def test_roll_multiple(self):
        count = 4
        result = self.dice.roll(count)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), count)
        for value in result:
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, self.dice.num_sides)





if __name__ == '__main__':
    unittest.main()
