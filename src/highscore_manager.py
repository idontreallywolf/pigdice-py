"""Manages highscores."""

import pickle
import os
import sys

from prettytable import PrettyTable, DOUBLE_BORDER, ALL

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class HighscoreManager:
    """Manages highscores."""

    def __init__(self):
        """Initialize internal highscore table."""
        self._highscores = {}
        self._scores_loaded = False

    def set_score_by_name(self, player_name, score):
        """Add a player and their score to the highscore table."""
        self._highscores[player_name] = max(score, 0)

    def get_score_by_name(self, player_name):
        """Return player score if exists, otherwise None."""
        return self._highscores.get(player_name)

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

    def get_top_scores(self, top_n: int = 3):
        """Return top `n` scores. `top_n = 3` by default."""
        sorted_highscores = sorted(
            self._highscores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_highscores[:top_n]

    def get_average_score(self):
        """Return the average of scores."""
        current_scores = self._highscores.values()
        total_of_scores = sum(current_scores)
        return total_of_scores / len(current_scores)

    def display_score_list(self):
        """Display highscores in a fancy ascii table."""
        table = PrettyTable(['Name', 'Score'])

        table.set_style(DOUBLE_BORDER)

        table.header = False
        table.title = 'Highscores'
        table.align['Name'] = 'l'
        table.align['Score'] = 'r'
        table.hrules = ALL

        for name, score in self._highscores.items():
            table.add_row((name, score))

        print(table.get_string(sortby='Score', reversesort=True))

    def _clear_all(self):
        self._highscores = {}
