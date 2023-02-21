import unittest
from src.dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()  # Create a Dice object
        
    def test_roll(self):
        # Test that rolling one dice gives correct result
        self.assertEqual(1 <= self.dice.roll() <= 6, True)
        # Test that rolling multiple times gives correct result
        roll_results = self.dice.roll(20)
        self.assertTrue(all([1 <= n <= 6 for n in roll_results]))
        
    def test_roll_count(self):
        d = Dice()

        # Test 1 value
        result = d.roll()
        self.assertTrue(0 < result <= 6)

        # Test multiple values 
        result = d.roll(5)
        self.assertEqual(len(result), 5)
        for num in result:
            self.assertTrue(0 < num <= 6)


if __name__ == '__main__':
    unittest.main()
