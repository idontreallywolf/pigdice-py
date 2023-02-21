import random


class Dice:
    num_sides = 6

    
    def __init__(self):
        pass


    def roll(self, count: int = 1) -> int | tuple[int]:
        '''Roll a random number, `1` to `6` inclusive.

        Parameters:
        `count`: how many dice to roll. Defaults to `1`.

        Returns:
        `int` or `tuple[int]` - containing dice value(s).
        '''
        
        rolls = tuple(random.randint(1, self.num_sides) for _ in range(count))
        if count == 1:
            return rolls[0]
        return rolls

    def __str__(self):
        """Override str method"""
        return f"Dice with {self.num_sides} sides"