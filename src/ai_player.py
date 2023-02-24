"""Represents the AI (Computer) player."""

from src.player import Player
from src.config import CHOICE_ROLL, CHOICE_HOLD

class AIPlayer(Player):
    """AI Player."""

    def __init__(self, threshold=20):
        """Initialize Player with name: AI and threshold value."""
        super().__init__('AI')
        self.threshold = threshold

    def make_choice(self, turn_score: int, oppenet_score: int) -> int:
        """Decription.

        Make a choice using pigdice game strategies.
        Parameters:
        turn_score: the current turn socre of the AI player.
        opponent_score: the total score of the opponent player.
        Returns:
        2 to hold, 1 to roll.
        """
        expected_score = self._get_expected_score(turn_score)
        if expected_score <= self.threshold:
            return CHOICE_HOLD
        return CHOICE_ROLL

    def _get_expected_score(self, turn_score: int) -> float:
        """How to do.

        Calulate the expected score for the current turn.
        Parameters:
        turn_score: the currenet turn score of the AI player

        Returns:
        float which is the exptedted score of the current turn.
        """
        num_sides = 6
        # the parameter is from dice class, but i don't know how to fix it
        except_scord = 0.0
        for i in range(1, num_sides + 1):
            p = 1 / num_sides
            #  Claculate the pdrobabilty of each possible outcome
            except_scord += (turn_score + i) * p
        return except_scord
