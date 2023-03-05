"""
The player module exports Player class which represents any player in the game.

Classes:
    `Player`
"""
import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import GAMEPLAY_CHOICE_ROLL, GAMEPLAY_CHOICE_HOLD
from src.dice import Dice


class Player:
    """
    This class provides methods to manage a player.

    Attributes:
        `_name` (`str`): The player's name.
        `_score` (`int`): The player's current score.
        `_temporary_score` (`int`): The player's temporary score for each roll.
        `_is_ai` (`bool`): True if the player is a Computer/AI.

    Methods:
        __init__(self, name: str, score: int = 0):
        Initializes the players.

        is_ai(self) -> bool: Returns True if the player is a Computer/AI.

        set_name(self, new_name: str) -> None:
        Sets the player's name to a new name.

        get_name(self) -> str:
        Returns the player's name.

        set_score(self, new_score: int) -> None:
        Sets the player's score to a new score.

        get_score(self) -> int:
        Returns the player's current score.

        add_temporary_score(self, score: int) -> None:
        Adds a score to the player's temporary score.

        get_temporary_score(self) -> int:
        Returns the player's temporary score.

        reset_temporary_score(self) -> None:
        Resets the player's temporary score.

        hold_score(self) -> None:
        Adds the player's temporary score to their current score.

        name_is_valid(name: str) -> bool:
        Returns True if the given name is valid.

        make_ai_choice(self) -> int | None:
        Makes a choice as an AI player,
        returning `GAMEPLAY_CHOICE_ROLL` or `None`.
    """

    def __init__(
        self,
        name: str,
        score: int = 0
    ):
        """
        Initialize a new instance of the Player class.

        Parameters:
            `name` (`str`): Player's name.
            `score` (`int`): Player's initial score. Default `0`

        Raises:
            ValueError: If length of `name` equals 0 or
            name` consists of spaces only.
        """
        if not Player.name_is_valid(name):
            raise ValueError('Invalid player name.')

        self._name = name
        self._score = max(score, 0)
        self._temporary_score = 0
        self._is_ai = name == "AI"

    def is_ai(self) -> bool:
        """
        Check whether the player is an AI.

        Returns:
            bool: `True` if player is Computer/AI.
        """
        return self._is_ai

    def set_name(self, new_name: str) -> None:
        """
        Set the player's name.

        Parameters:
            `new_name` (`str`): Player's new name.
        """
        self._name = new_name

    def get_name(self) -> str:
        """
        Get the player's name.

        Returns:
            `str`: Player's current name.
        """
        return self._name

    def set_score(self, new_score: int) -> None:
        """
        Set the player's score.

        Parameters:
            `new_score` (`int`): Player's new score.
        """
        self._score = max(new_score, 0)

    def get_score(self) -> int:
        """
        Get the player's current score.

        Returns:
            `int`: player's current score.
        """
        return self._score

    def add_temporary_score(self, score: int) -> None:
        """
        Add `score` to the player's temporary score.

        Parameters:
            `score` (`int`): Score to add.

        Returns:
            `None`
        """
        self._temporary_score += max(score, 0)

    def get_temporary_score(self) -> int:
        """
        Get the player's temporary score.

        Temporary score is the score which is stored for each roll.

        Returns:
            `int`: Player's temporary score.
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

        Parameters:
            `name` (`str`): name to be checked.

        Returns:
            `bool`: `True` if `name` has a length greater than 0
            and doesn't consist of only spaces.
        """
        return (len(name) > 0) and (not name.isspace())

    def make_ai_choice(self) -> int | None:
        """Make a choice as an AI player.

        Returns:
            `int` | `None`: Choice made by the AI player,
            or `None` if the player is not an AI.
        """
        if not self.is_ai():
            return None
        threshold = 10
        score = self.get_score()
        expected_score = self._get_expected_score(score)
        if expected_score <= threshold:
            return GAMEPLAY_CHOICE_HOLD

        # Implement AI strategy
        return GAMEPLAY_CHOICE_ROLL

    def _get_expected_score(self, current_score: int) -> float:
        """How to do.

        Calulate the expected score for the current turn.
        Claculate the pdrobabilty of each possible outcome
        Parameters:
        Score: the currenet score of the AI player
        Returns:
        float which is the exptedted score of the current turn.

        """
        except_scord = 0.0
        num_sides = Dice().num_sides
        for i in range(1, num_sides + 1):
            p = 1 / num_sides
            except_scord += (current_score + i) * p
        return except_scord
