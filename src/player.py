"""Player class represents a human player."""
import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import GAMEPLAY_CHOICE_ROLL


class Player:
    """Player class."""

    def __init__(
        self,
        name: str,
        score: int = 0
    ):
        """
        Initialize player's name, score and temporary score.

        Raises ValueError if length of `name` equals 0
        or `name` consists of spaces only.

        Parameters:
        `name`: Player's name.
        `score`: Player's initial score. Default `0`
        """
        if not Player.name_is_valid(name):
            raise ValueError('Invalid player name.')

        self._name = name
        self._score = max(score, 0)
        self._temporary_score = 0
        self._is_ai = name == "AI"

    def is_ai(self) -> bool:
        """Return `True` if player is Computer/AI."""
        return self._is_ai

    def set_name(self, new_name: str) -> None:
        """Set player's name to `new_name`."""
        self._name = new_name

    def get_name(self) -> str:
        """Get player's name."""
        return self._name

    def set_score(self, new_score: int) -> None:
        """Set player's name to `new_score`."""
        self._score = max(new_score, 0)

    def get_score(self) -> int:
        """Return player's current score."""
        return self._score

    def add_temporary_score(self, score: int) -> None:
        """Add `score` to temporary score."""
        self._temporary_score += max(score, 0)

    def get_temporary_score(self) -> int:
        """
        Get player's temporary score.

        Temporary score is the score which is stored for each roll.
        """
        return self._temporary_score

    def reset_temporary_score(self) -> None:
        """Reset temporary score."""
        self._temporary_score = 0

    def hold_score(self) -> None:
        """Increment player score by current temporary score."""
        self._score += self._temporary_score

    @staticmethod
    def name_is_valid(name: str) -> bool:
        """
        Check whether `name` is valid.

        It is valid if it has a length greater than 0 and
        doesn't consist of only spaces.
        """
        return (len(name) > 0) and (not name.isspace())

    def make_ai_choice(self) -> int | None:
        """Make a choice as AI player."""
        if not self.is_ai():
            return None

        # Implement AI strategy
        return GAMEPLAY_CHOICE_ROLL
