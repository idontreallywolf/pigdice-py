from prettytable import PrettyTable, DOUBLE_BORDER, ALL
import pickle
import os

class HighscoreManager:
    def __init__(self):
        self._highscores = {}
        self._scores_loaded = False

    def set_score_by_name(self, playerName, score):
        if (score < 0):
            score = 0

        self._highscores[playerName] = score

    def get_score_by_name(self, playerName):
        """Return player score if exists, otherwise None."""
        return self._highscores.get(playerName)

    def save_scores(self, file_path):
        """Save scores to a file, old data is overriden."""
        with open(file_path, 'wb+') as file:
            return pickle.dump(self._highscores, file)

    def load_scores(self, file_path) -> bool:
        """Load scores from file."""

        if not os.path.isfile(file_path):
            raise FileNotFoundError()

        # Prevent existing or updated scores from being overriden.
        if (self._scores_loaded):
            return False

        with open(file_path, 'rb') as file:
            self._highscores = pickle.load(file)
            self._scores_loaded = True

        return True

    def display_score_list(self):
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
