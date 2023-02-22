"""Contains configurations."""

import pathlib

MAX_PLAYERS = 2

CHOICE_ROLL = 1
CHOICE_HOLD = 2

GAME_INTRO = (
    "Welcome to the Tic-Tac-Toe. "
    "Type `help` or `?` to list commands.\n"
)

GAME_RULES = (
    (1, 'Rule one.', '⚠️ '),
    (2, 'Rule two.', '⚠️ '),
    (3, 'Rule three.', '⚠️ ')
)

GAME_MODE_MENU = (
    (1, 'Player vs Player', '😀'),
    (2, 'Player vs AI', '🤖'),
    (3, 'Cancel', '❌')
)

GAME_MODE_VS_PLAYER = 1
GAME_MODE_VS_AI = 2

GAMEPLAY_OPTIONS_MENU = (
    '1) HOLD ✊',
    '2) ROLL 🎲',
    '3) CHEAT ⏩',
    '4) END GAME ❌',
    '5) CHANGE NAME ✏️'
)

current_file_path = pathlib\
    .Path(__file__)\
    .parent.resolve()

DATA_PATH =\
    current_file_path\
    .joinpath('../data/')\
    .resolve()

SCORES_FILE_PATH = str(
    DATA_PATH
    .joinpath('scores.bin')
    .resolve()
)
