import unittest
import random
from src.dice import Dice


class TestDice(unittest.TestCase):
    def test_roll_count(self):
        d = Dice()

        # Test 1 value
        result = d.roll()
        self.assertEqual(0 < result <= 6)

        # Test multiple values 
        result = d.roll(5)
        self.assertEqual(len(result), 5)
        for num in result:
            self.assertTrue(0 < result <= 6)


if __name__ == '__main__':
    unittest.main()
