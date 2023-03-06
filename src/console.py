"""
Console module.

Console module is responsible for receiving and
processing user input while maintaining a loop.
"""
import cmd

import os
import sys

# Add the parent directory of the current file to the Python path :whygod:
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from colorama import\
    just_fix_windows_console,\
    Fore, Back, Style

from src.game import Game
from src.player import Player
from src.utils import make_table, animate_loading

from src.config import\
    GAME_MODE_MENU,\
    GAME_MODE_VS_PLAYER,\
    GAME_MODE_VS_AI,\
    GAME_RULES,\
    GAME_TURN_WON,\
    GAMEPLAY_CHOICE_END_GAME,\
    GAMEPLAY_CHOICE_CHANGE_NAME

just_fix_windows_console()


class Console(cmd.Cmd):
    """Docs for Console Class."""

    prompt = Fore.CYAN + '~ Console: ' + Style.RESET_ALL

    def __init__(self):
        """Initialize game and command API."""
        super().__init__()
        self.do_help(None)
        self.game = Game()
        self.game.load()

    def do_start(self, _):
        """Start the game."""
        table = make_table(
            'Choose a game mode',
            ['ID', 'Option', 'Icon']
        )
        table.add_rows(GAME_MODE_MENU)
        print(table)

        selected_game_mode = self._select_game_mode()
        self._setup_game(selected_game_mode)

    def do_highscore(self, _):
        """Show highscores."""
        scores_table = self.game.highscore_manager.get_scores_table()
        print(scores_table)

    def do_rules(self, _):
        """Show game rules."""
        print(GAME_RULES)

    def do_exit(self, _) -> bool:
        """
        Leave the game.

        Returns:
            `bool`: True
        """
        Console.print_danger('Exit Game.')
        return True

    def _select_game_mode(self) -> None:
        """
        Request player to select a game mode.

        Returns:
            `None`
        """
        return self._request_player_choice()

    def _setup_game(self, selected_game_mode: int) -> None:
        """
        Prepare game depending on `selected_game_mode`.

        Parameters:
            `selected_game_mode` (`int`):
            `GAME_MODE_VS_PLAYER` | `GAME_MODE_VS_AI`

        Returns:
            `None`
        """
        if selected_game_mode == GAME_MODE_VS_PLAYER:
            self._setup_pvp()
            return

        if selected_game_mode == GAME_MODE_VS_AI:
            self._setup_pva()
            return

        print('😔 Cancel setup.')

    def _setup_pvp(self) -> None:
        """Player vs Player setup."""
        for ordinal in range(1, 3):
            self._prepare_player(ordinal)

        self._game_loop()

    def _setup_pva(self) -> None:
        """Player vs AI setup."""
        self._prepare_player(ordinal=1)
        self.game.add_player(name='AI')
        self._game_loop()

    def _prepare_player(self, ordinal: int) -> None:
        """
        Prepare new player.

        Calls game's `add_player` method with player's chosen name as argument.

        Returns:
            `None`
        """
        self.game.add_player(
            self._request_player_name(ordinal)
        )

    def _request_player_name(self, ordinal: int) -> str:
        """
        Request player's name.

        Parameters:
            `ordinal` (`int`): player's ordinal. e.g (1)

        Returns:
            `str`: player's chosen name.
        """
        name = ''
        name_is_valid = Player.name_is_valid(name)
        while (not name_is_valid) or (name == "AI"):
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
            print("🤖 is thinking!!!")
            animate_loading()
            choice = current_player.make_ai_choice()
        else:
            choice = self._request_player_choice()

        # Player's input is then read by Game.parse_choice
        # and some decision is made based on that.
        self.game.parse_choice(choice)

        if choice == GAMEPLAY_CHOICE_CHANGE_NAME:
            new_name = None
            while True:
                new_name = input('Enter new name: ')
                if not Player.name_is_valid(new_name):
                    Console.print_danger('Invalid name, try again.')
                    continue

                changed = self.game.change_name(new_name)
                if not changed:
                    Console.print_danger('Name is already taken. Try another.')
                    continue
                Console.print_success(
                    f'Your name has been changed to "{new_name}"'
                )
                return self._game_loop()

        # In case the choice is to quit the game,
        # the player will be asked to confirm whether they
        # want to quit. When confirmed, the game will quit
        # and the player will see the initial interface.
        if choice == GAMEPLAY_CHOICE_END_GAME:
            confirmed = self._confirm('Are you sure?')
            if confirmed:
                self.game.quit()
                return True
            return self._game_loop()

        # After a player's turn, the turn status will be set.
        # It might be "won", "lost" or "neither".
        turn_status = self.game.get_turn_status()

        if turn_status == GAME_TURN_WON:
            print('🎉 Congratulations! You have won 🎉')
            self.game.save()
            self.game.quit()
            return True

        self._display_last_roll()

        return self._game_loop()

    def _confirm(self, message: str) -> bool:
        """
        Request confirmation from player.

        Parameters:
            `message`: The text which should be displayed in the prompt.
            e.g "Are you sure?"

        Returns:
            `bool`: `True` if the player chose `y`/`yes`.
        """
        print(message)

        choice = input('[Y/N] > ').lower()
        if choice in ('y', 'yes'):
            return True

        return False

    def _display_gameplay_options(self) -> None:
        """Show options available to the current player."""
        print(self.game.options_menu)

    def _display_current_player_turn(self) -> None:
        """Display text indicating current player's turn."""
        current_player: Player = self.game.get_current_player()
        name = current_player.get_name()

        print(f'{name}\'s turn.')
        temp_score = current_player.get_temporary_score()
        total_score = current_player.get_score()
        print(f'Your score: {temp_score}/{total_score}')

    def _request_player_choice(self) -> int:
        """
        Request player for an input.

        Returns:
            `int`: player's choice input.
        """
        while True:
            try:
                return int(input('Option > '))
            except ValueError:
                print('Invalid input. Try a number.')

    def _display_last_roll(self) -> None:
        """Show which number the player rolled."""
        last_roll = self.game.get_last_roll()
        if not last_roll:
            Console.print_default('You have chosen to hold.')
            return

        text = f'You rolled {last_roll}. 🎲'

        if last_roll > 1:
            Console.print_success(text)
            return

        Console.print_danger(text)

    @staticmethod
    def print_danger(text: str) -> None:
        """
        Print text with red background.

        Parameters:
        `text` (`str`): Text to be printed.
        """
        Console._print(f'{Back.RED}{Fore.WHITE}', text)

    @staticmethod
    def print_default(text: str) -> None:
        """
        Print text with red background.

        Parameters:
        `text` (`str`): Text to be printed.
        """
        Console._print(f'{Back.BLACK}{Fore.CYAN}', text)

    @staticmethod
    def print_success(text: str) -> None:
        """
        Print text with green background.

        Parameters:
        `text` (`str`): Text to be printed.
        """
        Console._print(Back.GREEN, text)

    @staticmethod
    def _print(style: str, text: str) -> None:
        """
        Print `text` with `style`.

        Parameters:
            `style` (`str`): background/foreground for the text to be printed.
            `text` (`str`): Text to be printed.
        """
        print(f'{style}\n\n{" " * 4}{text}\n{Style.RESET_ALL}\n')
