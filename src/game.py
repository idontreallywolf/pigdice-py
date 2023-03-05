"""exports Game class."""

import os
import sys

# Add the parent directory of the current file to the Python path :whygod:
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.player import Player
from src.highscore_manager import HighscoreManager
from src.dice import Dice
from src.utils import make_table

from src.config import\
    GAMEPLAY_OPTIONS_MENU,\
    GAMEPLAY_CHOICE_ROLL,\
    GAMEPLAY_CHOICE_HOLD,\
    GAMEPLAY_CHOICE_CHEAT,\
    GAME_TURN_WON,\
    GAME_TURN_LOST,\
    GAME_TURN_NEUTRAL,\
    SCORES_FILE_PATH


class Game:
    """
    This class represents the pigdice game and contains main game-logic.

    Attributes:
        highscore_manager (HighscoreManager):
        An instance of the HighscoreManager.

        options_menu (str):
        An ASCII table containing the available gameplay options.

        players (List[Player]):
        A list of Player objects representing players in the game.

        current_player (int):
        An integer index representing the index of the
        current player in the players list. Default `0`.

        last_roll (int):
        An integer representing the result of the last dice roll. Default `0`.

        turn_status (int):
        An integer representing the current status of the turn.
        Default `GAME_TURN_NEUTRAL`.

        Possible values are `GAME_TURN_WON`, `GAME_TURN_LOST`,
        and `GAME_TURN_NEUTRAL`.

    Methods:
        parse_choice(choice):
        Parses the player's choice and performs the appropriate action.

        load():
        Loads the high scores from the scores file.

        save():
        Saves the high scores of the current player to the scores file.

        add_player(name):
        Adds a new player to the game with the given name.

        change_turn():
        Changes the turn to the next player.

        get_current_player():
        Returns the current player object.
        Returns None if there are no players.

        set_turn_status(status):
        Sets the turn status to the given value.

        get_turn_status():
        Returns the current turn status.

        roll():
        Rolls the dice and updates the game state accordingly.

        hold():
        Holds the current score and changes to the next player.

        cheat():
        Gives the current player a score of 100 and ends the game.

        change_name(new_name):
        Changes the name of the current player.

        quit():
        Quits the game and resets the game state.

        set_last_roll(number):
        Sets the result of the last dice roll.

        get_last_roll():
        Returns the result of the last dice roll.
    """

    def __init__(self):
        """Initialize a new Game instance."""
        self.highscore_manager = HighscoreManager()
        self.options_menu = Game._prepare_options_menu()
        self.players = []
        self.current_player = 0
        self.last_roll = 0

        # The purpose of this state is to keep track of
        # whether the current player has won, lost, or neither.
        # Default: GAME_TURN_NEUTRAL
        self.turn_status:\
            GAME_TURN_WON |\
            GAME_TURN_LOST |\
            GAME_TURN_NEUTRAL\
            = GAME_TURN_NEUTRAL

    def parse_choice(self, choice: int) -> None:
        """
        Parse the player's choice and take appropriate action.

        Parameters:
            `choice` (`int`): an integer representing the player's choice.

        Returns:
            `None`
        """
        if choice == GAMEPLAY_CHOICE_ROLL:
            self.roll()
            return

        if choice == GAMEPLAY_CHOICE_HOLD:
            self.hold()
            return

        if choice == GAMEPLAY_CHOICE_CHEAT:
            self.cheat()

    def load(self) -> None:
        """
        Load the highscores.

        Internally calling highscore manager's load_scores.

        Returns:
            None
        """
        try:
            self.highscore_manager.load_scores(SCORES_FILE_PATH)
        except FileNotFoundError:
            pass

    def save(self) -> None:
        """
        Save the highscores of players in the current game.

        Inernally calls highscore manager's `save_scores` method.

        Returns:
            None
        """
        self.highscore_manager.save_scores(SCORES_FILE_PATH)

    def add_player(self, name: str) -> None:
        """
        Add new player to the game.

        Parameters:
            `name` (`str`): the name of the new player

        Returns:
            None
        """
        self.players.append(Player(name))

    def change_turn(self) -> None:
        """
        Change game turn to the next player.

        Toggles `current_player`'s value to `0` or `1`

        Returns:
            `None`
        """
        if self.current_player == 0:
            self.current_player = 1
            return

        self.current_player = 0

    def get_current_player(self) -> Player | None:
        """
        Get current player.

        Returns:
        `Player`: the current player, or None if there are no players.
        """
        if len(self.players) == 0:
            return None

        return self.players[self.current_player]

    def set_turn_status(self, status) -> None:
        """
        Set game `turn_status`.

        Parameters:
            `status` (`int`): the status of the turn
            (either `GAME_TURN_WON`, `GAME_TURN_LOST`, or `GAME_TURN_NEUTRAL`)
        """
        self.turn_status = status

    def get_turn_status(self) -> int:
        """
        Get the status of the current turn.

        Returns:
            `int`: the status of the turn
            (either `GAME_TURN_WON`, `GAME_TURN_LOST`, or `GAME_TURN_NEUTRAL`)
        """
        return self.turn_status

    def roll(self):
        """
        Roll the dice and update the game state.

        If the dice value is `1` the player loses and
        game turn is set to `GAME_TURN_LOST`.

        Otherwise, the status will remain as `GAME_TURN_NEUTRAL`
        unless the player's current score + total score >= 100,
        in which case the `turn_status` is set to `GAME_TURN_WON.`

        When the user has won, internally calls highscore_manager's
        `create_record` method in order to save both players' scores.

        Returns: `None`
        """
        player: Player = self.get_current_player()

        roll_result = Dice().roll()
        self.set_last_roll(roll_result)

        if roll_result == 1:
            self.set_turn_status(GAME_TURN_LOST)
            self.change_turn()
            player.reset_temporary_score()
            return

        player.add_temporary_score(roll_result)
        total_score = player.get_temporary_score() + player.get_score()
        if total_score >= 100:
            player.set_score(total_score)
            self.set_turn_status(GAME_TURN_WON)
            self.highscore_manager.create_record(self.players)
            return

        self.set_turn_status(GAME_TURN_NEUTRAL)

    def hold(self) -> None:
        """
        Hold player's current turn-based score.

        Calls current player's `hold_score` method which adds
        player's turn-score to their total-score.

        Sets `last_roll` to `None`.

        Calls `change_turn`.

        Returns:
            `None`
        """
        player: Player = self.get_current_player()
        player.hold_score()
        player.reset_temporary_score()
        self.set_turn_status(GAME_TURN_NEUTRAL)
        self.set_last_roll(None)
        self.change_turn()

    def cheat(self) -> None:
        """
        Grant maximum score to current player.

        Sets player's total-score to `100`,
        updates `turn_status` to `GAME_TURN_WON`
        and creates a highscore record by calling
        HighscoreManager's create_record method.
        """
        player: Player = self.get_current_player()
        player.set_score(100)
        self.set_turn_status(GAME_TURN_WON)
        self.highscore_manager.create_record(self.players)

    def change_name(self, new_name: str) -> bool:
        """
        Change player's name during the game.

        Attempts to change player's name to `new_name`.

        If `new_name` is already taken by another player,
        then the process will fail.

        Parameters:
            `new_name` (`str`): player's new name.

        Returns:
            `True` if `new_name` is not taken.
        """
        for player in self.players:
            if player.get_name() == new_name:
                return False

        player: Player = self.get_current_player()
        name = player.get_name()
        changed = self.highscore_manager.change_name(name, new_name)
        if not changed:
            return False

        player.set_name(new_name)
        return True

    def quit(self) -> None:
        """
        Quit the game.

        Resets game state.

        Returns:
            `None`
        """
        self.players = []
        self.current_player = 0
        self.turn_status = GAME_TURN_NEUTRAL
        self.last_roll = 0

    def set_last_roll(self, number: int) -> None:
        """
        Set the last dice number.

        Parameters:
        `number` (`int`): last rolled dice's value.

        Returns:
            `None`
        """
        self.last_roll = number

    def get_last_roll(self) -> int:
        """
        Get the latest dice number stored.

        Returns:
            `int`: latest dice's value.
        """
        return self.last_roll

    @staticmethod
    def _prepare_options_menu():
        """
        Prepare options menu.

        Returns:
            an ASCII table containing gameplay options menu.
        """
        table = make_table(
            title="Options",
            columns=['ID', 'Label', 'Icon']
        )

        for option in GAMEPLAY_OPTIONS_MENU:
            table.add_row(option)

        return table
