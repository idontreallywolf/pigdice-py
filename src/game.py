"""Module docstring."""

from player import Player
from ai_player import AIPlayer
from highscore_manager import HighscoreManager

from prettytable import\
    PrettyTable,\
    DOUBLE_BORDER,\
    ALL

from config import\
    GAMEPLAY_OPTIONS_MENU,\
    GAMEPLAY_CHOICE_ROLL,\
    GAMEPLAY_CHOICE_HOLD,\
    GAME_TURN_WON,\
    GAME_TURN_LOST,\
    GAME_TURN_NEUTRAL


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
        if choice == GAMEPLAY_CHOICE_ROLL:
            self.roll()
            return

        if choice == GAMEPLAY_CHOICE_HOLD:
            self.hold()
            return

    def load(self):
        # TODO: This method should be called during initialization.
        #
        # Call highscore_manager's load_scores method
        # with the argument SCORES_FILE_PATH constant (from config)
        # note: method can raise FileNotFoundError
        pass

    def save(self):
        # TODO: This method should save highscores by calling
        # highscore_manager's save_scores method
        # with the argument SCORES_FILE_PATH constant (from config)
        pass

    def add_player(self, name):
        """Add new player to the game."""
        self.players.append(Player(name))

    def add_ai_player(self):
        """Add new AI player to the game."""
        self.players.append(AIPlayer())

    def get_current_player(self):
        """Get current player."""
        # TODO: This method should return the current player.
        pass

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
        """Roll dice."""
        # TODO: This method should implement
        # rolling dice for current player.
        pass

    def hold(self):
        """Hold current score."""
        # TODO: This method should implement
        # holding dice for current player.
        pass

    def cheat(self):
        """Grant maximum score to current player."""
        # TODO: This method should let
        # the player reach maximum score to win.
        pass

    def change_name(self, new_name):
        # TODO: This method should change the name
        # of the current player to `new_name`.
        pass

    def quit(self):
        # TODO: This method should
        # 1) ask the player to confirm.
        #    if player confirms, then proceed.
        # 2) call save method in order to save anything that should be saved.
        pass

    def make_table(title, columns: list[str]) -> PrettyTable:
        """Build and return an ASCII table."""
        table = PrettyTable(columns)

        table.set_style(DOUBLE_BORDER)
        table.header = False
        table.title = title or "Title"
        table.hrules = ALL

        return table

    def _prepare_options_menu():
        """Return an ASCII table containing gameplay options menu."""
        table = Game.make_table(
            title="Options",
            columns=['ID', 'Label', 'Icon']
        )

        for option in GAMEPLAY_OPTIONS_MENU:
            table.add_row(option)

        return table
