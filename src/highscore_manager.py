"""Manages highscores."""

import pickle
import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils import make_table
from src.player import Player


class HighscoreManager:
    """Manages highscores."""

    def __init__(self):
        """Initialize internal highscore table."""
        self._highscores = []
        self._scores_loaded = False
        self.table = make_table(
            'Highscores',
            ['P1', 'Score', 'P2', 'Score2']
        )

    def prepare_table(self):
        """Prepare highscores table."""
        self.table.align['P1'] = 'l'
        self.table.align['Score'] = 'r'
        self.table.align['P2'] = 'l'
        self.table.align['Score2'] = 'r'

    def change_name(self, old_name, new_name):
        """
        Update player's name, including old games.

        Return: `true` if successful.
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

    def name_exists(self, player_name) -> bool:
        """
        Check whether player name exists/ is taken.

        Return: `true` if exists.
        """
        for game in self._highscores:
            for name, _ in game.items():
                if player_name == name:
                    return True
        return False

    def create_record(self, players: list[Player]):
        """Create new highscore record."""
        new_record = {}

        for player in players:
            new_record[player.get_name()] = player.get_score()

        self._highscores.append(new_record)

    def save_scores(self, file_path):
        """Save scores to a file, old data is overriden."""
        with open(file_path, 'wb+') as file:
            return pickle.dump(self._highscores, file)

    def load_scores(self, file_path) -> bool:
        """Load scores from file."""
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
        Display highscores in a fancy ascii table.

        Return: String representation of the highscores table.
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
        self._highscores = []
