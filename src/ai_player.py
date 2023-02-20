from player import Player
from config import CHOICE_ROLL, CHOICE_HOLD

class AIPlayer(Player):
    def __init__(self):
        super().__init__('AI')
    
    def make_choice(self) -> int:
        # TODO: Implement AI strategy
        return CHOICE_ROLL
