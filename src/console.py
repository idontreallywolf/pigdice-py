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
    GAME_RULES,\
    GAME_TURN_WON,\
    GAME_TURN_LOST,\
    GAMEPLAY_CHOICE_END_GAME


class Console(cmd.Cmd):
    """Docs for Console Class."""

    prompt = '~ Console: '

    def __init__(self):
        """Initialize game and command API."""
        super().__init__()
        self.do_help(None)
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
        """Show game rules."""
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
        self._prepare_player(ordinal=1)
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
            name = input(f'Player {ordinal}\'s name: ')
            name_is_valid = Player.name_is_valid(name)

        return name

    def _game_loop(self):
        self._display_current_player_turn()

        # This is the menu of options that will be shown to the player
        # while they are playing. A player may choose to roll, hold, quit etc.
        self._display_gameplay_options()

        # After displaying the options, the player is requested to provide
        # an input.
        choice = self._request_player_choice()

        # Player's input is then read by Game.parse_choice
        # and some decision is made based on that.
        self.game.parse_choice(choice)

        # In case the choice is to quit the game,
        # the player will be asked to confirm whether they
        # want to quit. When confirmed, the game will quit
        # and the player will see the initial interface.
        if choice == GAMEPLAY_CHOICE_END_GAME:
            confirmed = self._confirm('Are you sure?')
            if confirmed:
                self.game.quit()
                return True

        # After a player's turn, the turn status will be set.
        # It might be "won", "lost" or "neither".
        turn_status = self.game.get_turn_status()

        if turn_status == GAME_TURN_WON:
            print('🎉 Congratulations! You have won 🎉')
            self.game.save()
            self.game.quit()
            return True

        if turn_status == GAME_TURN_LOST:
            print('😔 You rolled a 1!\n')

        self._game_loop()

    def _confirm(self, message):
        """
        Request confirmation from player.

        Parameters:
        `message`: The text which should be displayed in the prompt. e.g "Are you sure?"
        """
        print(message)

        choice = input('[Y/N] > ').lower()
        if choice in ('y', 'yes'):
            return True

        return False

    def _display_gameplay_options(self):
        """Show options available to the current player."""
        print(self.game.options_menu)

    def _display_current_player_turn(self):
        """Display text indicating current player's turn."""
        current_player: Player = self.game.get_current_player()
        name = current_player.get_name()
        print(f'{name}\'s turn.')

    def _request_player_choice(self):
        while True:
            try:
                return int(input('Option > '))
            except ValueError:
                print('Invalid input. Try a number.')
