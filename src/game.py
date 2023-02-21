"""Module docstring."""

from highscore_manager import HighscoreManager
# pylint: disable=too-few-public-methods


class Game:
    """Docs for Game Class."""

    def __init__(self):
        """Initialize Game."""
        self.highscore_manager = HighscoreManager()

        # Keeps track of Players who are currently playing.
        self.players = []

        # Stores the index for current player.
        self.current_player = 0

