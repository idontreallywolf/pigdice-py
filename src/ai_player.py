"""Represents the AI (Computer) player."""

from player import Player
from config import CHOICE_ROLL


class AIPlayer(Player):
    """AI Player."""

    def __init__(self):
        """Initialize Player with name: AI."""
        super().__init__('AI')

    def make_choice(self) -> int:
        """Make a choice using pigdice game strategies."""
        # TODO: Implement AI strategy
        return CHOICE_ROLL
