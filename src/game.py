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

    def get_current_player(self):
        """Get current player."""
        # TODO: This method should return the current player.
        pass

    def roll(self):
        """Roll dice."""
        # TODO: This method should implement
        # rolling dice for current player.
        pass

    def hold(self):
        """Hold current score."""
        # TODO: This method should implement
        # holding dice for current player.
        pass

    def has_won(self):
        """Check whether current player has won the game."""
        # TODO: This method check
        # whether the current player has won.
        pass

    def cheat(self):
        """Grant maximum score to current player."""
        # TODO: This method should let
        # the player reach maximum score to win.
        pass

    def change_name(self, new_name):
        # TODO: This method should change the name
        # of the current player to `new_name`.
        pass
