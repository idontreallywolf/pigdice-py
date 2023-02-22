"""Module docstring."""

from player import Player
from ai_player import AIPlayer
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

    def load(self):
        # TODO: This method should be called during initialization.
        #
        # Call highscore_manager's load_scores method
        # with the argument SCORES_FILE_PATH constant (from config)
        # note: method can raise FileNotFoundError
        pass

    def save(self):
        # TODO: This method should save highscores by calling
        # highscore_manager's save_scores method
        # with the argument SCORES_FILE_PATH constant (from config)
        pass

    def add_player(self, name):
        """Add new player to the game."""
        self.players.append(Player(name))

    def add_ai_player(self):
        """Add new AI player to the game."""
        self.players.append(AIPlayer())

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

    def quit(self):
        # TODO: This method should
        # 1) ask the player to confirm.
        #    if player confirms, then proceed.
        # 2) call save method in order to save anything that should be saved.
        pass

    def make_table(title, columns: list[str]) -> PrettyTable:
        """Build and return an ASCII table."""
        table = PrettyTable(columns)

        table.set_style(DOUBLE_BORDER)
        table.header = False
        table.title = title or "Title"
        table.hrules = ALL

        return table
