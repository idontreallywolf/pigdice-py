"""
Console module.

Console module is responsible for receiving and
processing user input while maintaining a loop.
"""
import cmd

from colorama import\
    just_fix_windows_console,\
    Fore, Back, Style

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

just_fix_windows_console()


class Console(cmd.Cmd):
    """Docs for Console Class."""

    prompt = Fore.CYAN + '~ Console: ' + Style.RESET_ALL

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

    def do_highscore(self, _):
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
        print(Back.LIGHTRED_EX + "Exit Game." + Style.RESET_ALL)
        return True

    def _select_game_mode(self):
        return self._request_player_choice()

    def _setup_game(self, selected_game_mode):
        if selected_game_mode == GAME_MODE_VS_PLAYER:
            self._setup_pvp()
            return

        if selected_game_mode == GAME_MODE_VS_AI:
            self._setup_pva()
            return

        print('😔 Cancel setup.')

    def _setup_pvp(self):
        """Player vs Player setup."""
        for ordinal in range(1, 3):
            self._prepare_player(ordinal)

        self._game_loop()

    def _setup_pva(self):
        """Player vs AI setup."""
        self._prepare_player(ordinal=1)
        self.game.add_player(name='AI')
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
        # This is the menu of options that will be shown to the player
        # while they are playing. A player may choose to roll, hold, quit etc.
        self._display_gameplay_options()

        self._display_current_player_turn()

        # After displaying the options, the player is requested to provide
        # an input.
        current_player: Player = self.game.get_current_player()
        choice = None
        if current_player.is_ai():
            choice = current_player.make_ai_choice()
        else:
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
            print(f'{current_player.get_name()} rolled a 1!\n')

        self.game.change_turn()

        return self._game_loop()

    def _confirm(self, message):
        """
        Request confirmation from player.

        Parameters:
        `message`: The text which should be displayed in the prompt.
        e.g "Are you sure?"
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
