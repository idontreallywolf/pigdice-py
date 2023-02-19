import random


class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self, count: int = 1) -> int | tuple[int]:
        '''Roll a random number, `1` to `6` inclusive.
        
        Parameters:\n
        `count`: how many dice to roll. Defaults to `1`.

        Returns:\n
        `int` or `tuple[int]` - containing dice value(s).
        '''
        rolls = tuple(random.randint(1, self.num_sides) for _ in range(count))
        if count == 1:
            return rolls[0]
        return rolls
