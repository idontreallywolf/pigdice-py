"""
Console module is responsible for receiving and
processing user input while maintaining a loop.
"""

import cmd
import game
from config import\
    GAME_INTRO,\
    GAME_RULES


class Console(cmd.Cmd):
    """Docs for Console Class."""

    intro = GAME_INTRO
    prompt = '~ Console: '

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

    def do_read_rules(self):
        print(*GAME_RULES)

    def do_exit(self, _):
        """Leave the game."""
        print("Exit Game.")
        return True
