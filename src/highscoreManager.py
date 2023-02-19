from prettytable import PrettyTable, DOUBLE_BORDER, ALL

class HighscoreManager:
    _highscores = {}

    def set_score_by_name(self, playerName, score):
        if (score < 0):
            score = 0

        self._highscores[playerName] = score

    def get_score_by_name(self, playerName):
        """Return player score if exists, otherwise None."""
        return self._highscores.get(playerName)


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
