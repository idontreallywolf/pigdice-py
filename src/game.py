"""Module docstring."""
from prettytable import\
    PrettyTable,\
    DOUBLE_BORDER,\
    ALL

from colorama import\
    just_fix_windows_console,\
    Fore, Style

from src.player import Player
from src.highscore_manager import HighscoreManager
from src.dice import Dice

from src.config import\
    GAMEPLAY_OPTIONS_MENU,\
    GAMEPLAY_CHOICE_ROLL,\
    GAMEPLAY_CHOICE_HOLD,\
    GAME_TURN_WON,\
    GAME_TURN_LOST,\
    GAME_TURN_NEUTRAL,\
    SCORES_FILE_PATH

just_fix_windows_console()


class Game:
    """Docs for Game Class."""

    def __init__(self):
        """Initialize Game."""
        self.highscore_manager = HighscoreManager()
        self.options_menu = Game._prepare_options_menu()
        self.players = []
        self.current_player = 0

        # The purpose of this state is to remember whether
        # the current player has won, lost, or neither.
        # Default: GAME_TURN_NEUTRAL
        self.turn_status:\
            GAME_TURN_WON |\
            GAME_TURN_LOST |\
            GAME_TURN_NEUTRAL\
            = GAME_TURN_NEUTRAL

    def parse_choice(self, choice):
        """Parse player's choice."""
        if choice == GAMEPLAY_CHOICE_ROLL:
            self.roll()
            return

        if choice == GAMEPLAY_CHOICE_HOLD:
            self.hold()
            return

        if choice == GAMEPLAY_CHOICE_CHEAT:
            self.cheat()

    def load(self):
        """Load score."""
        try:
            self.highscore_manager.load_scores(SCORES_FILE_PATH)
        except FileExistsError:
            print("The scores file could not be found!")

    def save(self):
        """Save highscores of current player."""
        self.highscore_manager.save_scores(SCORES_FILE_PATH)

    def add_player(self, name):
        """Add new player to the game."""
        self.players.append(Player(name))

    def change_turn(self):
        """Change player's turn."""
        if self.current_player == 0:
            self.current_player = 1
            return

        self.current_player = 0

    def get_current_player(self) -> Player | None:
        """
        Get current player.

        Returns None if there are no players.
        """
        if len(self.players) == 0:
            return None

        return self.players[self.current_player]

    def set_turn_status(self, status):
        """
        Set game `turn_status`.

        Possible values: `GAME_TURN_WON | GAME_TURN_LOST | GAME_TURN_NEUTRAL`
        """
        self.turn_status = status

    def get_turn_status(self):
        """
        Return curren turn's status.

        `GAME_TURN WON | GAME_TURN_LOST | GAME_TURN_NEUTRAL`
        """
        return self.turn_status

    def roll(self):
        """Roll a dice."""
        player: Player = self.get_current_player()

        roll_result = Dice().roll()
        if roll_result == 1:
            self.set_turn_status(GAME_TURN_LOST)
            self.change_turn()
            player.reset_temporary_score()
            return

        player.add_temporary_score(roll_result)
        if player.get_temporary_score() + player.get_score() >= 100:
            self.set_turn_status(GAME_TURN_WON)
            return

        self.set_turn_status(GAME_TURN_NEUTRAL)

    def hold(self):
        """Hold current score."""
        player: Player = self.get_current_player()
        player.hold_score()
        player.reset_temporary_score()
        self.set_turn_status(GAME_TURN_NEUTRAL)
        self.change_turn()

    def cheat(self):
        """Grant maximum score to current player."""
        player: Player = self.get_current_player()
        player.set_score(100)
        self.set_turn_status(GAME_TURN_WON)

    def change_name(self, new_name):
        """Change player's name during the game."""
        player: Player = self.get_current_player()
        player.set_name(new_name)

    def quit(self):
        """Quit the game."""
        self.players = []
        self.current_player = 0
        self.turn_status = GAME_TURN_NEUTRAL

    @staticmethod
    def make_table(title, columns: list[str]) -> PrettyTable:
        """Build and return an ASCII table."""
        table = PrettyTable(columns)

        table.set_style(DOUBLE_BORDER)
        table.header = False
        table.title =\
            Fore.CYAN +\
            (title or "Title") +\
            Style.RESET_ALL
        table.hrules = ALL

        return table

    @staticmethod
    def _prepare_options_menu():
        """Return an ASCII table containing gameplay options menu."""
        table = Game.make_table(
            title="Options",
            columns=['ID', 'Label', 'Icon']
        )

        for option in GAMEPLAY_OPTIONS_MENU:
            table.add_row(option)

        return table
