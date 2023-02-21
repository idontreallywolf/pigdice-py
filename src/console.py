"""
Console module is responsible for receiving and
processing user input while maintaining a loop.
"""

import cmd
import game


class Console(cmd.Cmd):
    """Docs for Console Class."""

    intro = (
        "Welcome to the Tic-Tac-Toe. "
        "Type `help` or `?` to list commands.\n"
    )

    prompt = "~ Console: "

    def __init__(self):
        """Initialize game and command API."""
        super().__init__()
        self.game = game.Game()

    def do_start(self):
        """Start the game."""
        return True

    def do_highscore(self):
        """Show highscores."""
        return True

    def do_exit(self, _):
        """Leave the game."""
        print("Exit Game.")
        return True
