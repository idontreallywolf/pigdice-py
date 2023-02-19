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
        length_of_longest_name = self._length_of_longest_name()
        length_of_longest_score = self._length_of_longest_score()

        highscore_table = self._prepare_table(
            length_of_longest_name,
            length_of_longest_score
        )

        print(highscore_table)

    def _clear_all(self):
        self._highscores = {}

    def _length_of_longest_name(self):
        player_names = list(self._highscores.keys())
        return self._length_of_longest_element(player_names)

    def _length_of_longest_score(self):
        player_scores = list(self._highscores.values())
        return self._length_of_longest_element(player_scores)

    def _length_of_longest_element(self, items):
        """
        Return the length of the string representation of the element with most characters.\n
        Example: for the list ('one','two','three','four'):\n
        length of 'three', `5`, will be returned
        """
        string_length = 0

        for string in items:
            string = str(string)
            if len(string) > string_length:
                string_length = len(string)

        return string_length

    def _prepare_table(self, longest_name_length, longest_score_length):
        cell_padding = 1
        table_width =\
            longest_name_length +\
            longest_score_length +\
            (cell_padding * 2) +\
            (cell_padding * 2)

        table_header = '{0}{1}{2}'.format('╔', table_width * '═', '╗')
        table_title = '{:^{padding}s}'.format(
            'Highscores',
            padding=table_width
        )
        """
        header = "╔═══╦═══╦═══╗\n"
        row_separator = "╠═══╬═══╬═══╣\n"

        cell_separator = "║" # add "\n" after last wall/separator
        footer = "╚═══╩═══╩═══╝\n"
        ╔═══════════════════╗
        ║    Highscores     ║
        ╠════════════╦══════╣
        ║ PlayerN    ║ 1234 ║
        ╠════════════╬══════╣
        ║ PlayerName ║  234 ║
        ╚════════════╩══════╝
        """
