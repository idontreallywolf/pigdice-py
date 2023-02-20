from player import Player

class Choice:
    HOLD: int = 1
    ROLL: int = 2

class AIPlayer(Player):
    def __init__(self):
        super().__init__('AI')
    
    def make_choice(self) -> int:
        # TODO: Implement AI strategy
        return Choice.ROLL
