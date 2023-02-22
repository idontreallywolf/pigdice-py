"""
Console module is responsible for receiving and
processing user input while maintaining a loop.
"""

import cmd
from game import Game
from player import Player

from config import\
    GAME_MODE_MENU,\
    GAME_MODE_VS_PLAYER,\
    GAME_MODE_VS_AI,\
    GAME_INTRO,\
    GAME_RULES


class Console(cmd.Cmd):
    """Docs for Console Class."""

    intro = GAME_INTRO
    prompt = '~ Console: '

    def __init__(self):
        """Initialize game and command API."""
        super().__init__()
        self.game = Game()

    def do_start(self, _):
        """Start the game."""
        table = Game.make_table(
            'Choose a game mode',
            ['ID', 'Option', 'Icon']
        )
        table.add_rows(GAME_MODE_MENU)
        print(table)

        selected_game_mode = self._select_game_mode()
        self._setup_game(selected_game_mode)

    def do_highscore(self):
        """Show highscores."""
        return True

    def do_rules(self, _):
        table = Game.make_table(
            'Game Rules',
            ['ID', 'Rule', 'Icon']
        )
        table.add_rows(GAME_RULES)
        print(table)

    def do_exit(self, _):
        """Leave the game."""
        print("Exit Game.")
        return True

    def _select_game_mode(self):
        while True:
            try:
                return int(input('> '))
            except ValueError:
                print('[Error]: Invalid input. Try a number.')

    def _setup_game(self, selected_game_mode):
        if selected_game_mode == GAME_MODE_VS_PLAYER:
            return self._setup_pvp()

        if selected_game_mode == GAME_MODE_VS_AI:
            return self._setup_pva()

        print('😔 Cancel setup.')

    def _setup_pvp(self):
        """Player vs Player setup."""
        for ordinal in range(1, 3):
            self._prepare_player(ordinal)

        self._game_loop()

    def _setup_pva(self):
        """Player vs AI setup."""
        self._prepare_player(1)
        self.game.add_ai_player()
        self._game_loop()

    def _prepare_player(self, ordinal):
        """Prepare new player."""
        self.game.add_player(
            self._request_player_name(ordinal)
        )

    def _request_player_name(self, ordinal):
        """Request player's name."""
        name = ''
        name_is_valid = Player.name_is_valid(name)
        while not name_is_valid:
            name = input('Player {}\'s name: '.format(ordinal))
            name_is_valid = Player.name_is_valid(name)

        return name

    def _game_loop(self):
        # TODO: Implement game loop.
        print('GAME LOOP. To be Implemented.')
        return True
