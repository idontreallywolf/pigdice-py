"""Module docstring."""

from player import Player
from highscore_manager import HighscoreManager
from dice import Dice
from config import SCORES_FILE_PATH
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
        """Load score."""
        try:
            self.highscore_manager.load_scores(SCORES_FILE_PATH)
        except FileExistsError:
            print("The scores file could not be found!")

    def save(self):
        """Save highscores of current player."""
        self.highscore_manager.save_scores(SCORES_FILE_PATH)

    def add_player(self, name):
        """Add new player to the game."""
        self.players.append(Player(name))

    def get_current_player(self):
        """Get current player."""
        return self.players[self.current_player]

    def roll(self):
        """Roll a dice."""
        player: Player = self.get_current_player()
        roll_result = Dice().roll()
        if roll_result == 1:
            return player.reset_temporary_score()
        return player.add_temporary_score(roll_result)

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
        player: Player = self.get_current_player()
        player.set_score(100)

    def change_name(self, new_name):
        # TODO: This method should change the name
        # of the current player to `new_name`.
        pass

    def quit_game(self):
        # TODO: This method should
        # 1) ask the player to confirm.
        #    if player confirms, then proceed.
        # 2) call save method in order to save anything that should be saved.
        pass
