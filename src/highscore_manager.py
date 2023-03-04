"""Manages highscores."""

import pickle
import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils import make_table
from src.player import Player


class HighscoreManager:
    """
    A class for managing highscores in a game.

    Attributes:
        _highscores (list[dict]):
            Internal highscore table.

        _scores_loaded (bool):
            Indicator of whether scores have been loaded from file.

        table (PrettyTable):
            Table used to display highscores in a fancy ascii table.

    Methods:
        __init__():
            Initializes internal highscore table,
            sets _scores_loaded to False, and
            creates a PrettyTable object for display.

        prepare_table():
            Aligns columns in the table object.

        change_name(old_name: str, new_name: str) -> bool:
            Updates player's name, including old games.
            Returns True if successful.

        name_exists(player_name: str) -> bool:
            Checks whether player name exists/is taken.
            Returns True if exists.

        create_record(players: list[Player]):
            Creates new highscore record.

        save_scores(file_path: str):
            Saves scores to a file,
            overwriting old data.

        load_scores(file_path: str) -> bool:
            Loads scores from file.
            Returns True if successful.

        get_scores_table() -> str:
            Displays highscores in a fancy ascii table.
            Returns string representation of the table.

        _clear_all():
            Clears all highscores.
    """

    def __init__(self):
        """Initialize internal highscore table."""
        self._highscores = []
        self._scores_loaded = False
        self.table = make_table(
            'Highscores',
            ['P1', 'Score', 'P2', 'Score2']
        )

    def prepare_table(self) -> None:
        """Prepare highscores table."""
        self.table.align['P1'] = 'l'
        self.table.align['Score'] = 'r'
        self.table.align['P2'] = 'l'
        self.table.align['Score2'] = 'r'

    def change_name(self, old_name: str, new_name: str) -> bool:
        """
        Change player's name, including old games.

        Parameters:
            `old_name` (`str`): The old name of the player.
            `new_name` (`str`): The new name of the player.

        Returns:
            `bool`: `True` if successful.
            `False` if `new_name` is already taken.
        """
        if self.name_exists(new_name):
            return False

        temp_list = []

        for game in self._highscores:
            temp_game = {}
            for name in game.keys():
                if old_name == name:
                    temp_game[new_name] = game[old_name]
                    continue

                temp_game[name] = game[name]

            temp_list.append(temp_game)
        self._highscores = temp_list
        return True

    def name_exists(self, player_name: str) -> bool:
        """
        Check whether player name exists/is taken.

        Parameters:
            `player_name` (`str`): name that is to be checked.

        Returns:
            bool: True if exists.
        """
        for game in self._highscores:
            for name, _ in game.items():
                if player_name == name:
                    return True
        return False

    def create_record(self, players: list[Player]) -> None:
        """
        Create new highscore record.

        Parameters:
            `players` (`list[Player]`): List of players in the game.

        Returns:
            `None`
        """
        new_record = {}

        for player in players:
            new_record[player.get_name()] = player.get_score()

        self._highscores.append(new_record)

    def save_scores(self, file_path: str) -> None:
        """
        Save scores to a file, old data is overridden.

        Parameters:
            `file_path` (`str`): The path to the file to save the scores to.

        Returns:
            `None`
        """
        with open(file_path, 'wb+') as file:
            pickle.dump(self._highscores, file)

    def load_scores(self, file_path) -> bool:
        """
        Load scores from a file.

        Parameters:
            `file_path` (`str`): The path to the file containing the scores.

        Returns:
            `bool`: `True` if the scores were successfully loaded,
            `False` otherwise.

        Raises:
            `FileNotFoundError`: If the specified file could not be found.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError()

        # Prevent existing or updated scores from being overriden.
        if self._scores_loaded:
            return False

        with open(file_path, 'rb') as file:
            self._highscores = pickle.load(file)
            self._scores_loaded = True

        return True

    def get_scores_table(self):
        """
        Display highscores in a formatted ASCII table.

        Returns:
            `str`: A string representation of the highscores table.
        """
        self.table.clear_rows()

        if len(self._highscores) == 0:
            # temporary empty row
            self.table.add_row((' ', ' ', ' ', ' '))
            return self.table.get_string()

        for game_round in self._highscores:
            row = []
            for name, score in game_round.items():
                row.append(name)
                row.append(score)
            self.table.add_row(row)

        return self.table.get_string()

    def _clear_all(self):
        """Clear highscores."""
        self._highscores = []
