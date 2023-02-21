"""Contains configurations."""

import pathlib

PLAYER_X = 'x'
PLAYER_O = 'o'

CHOICE_ROLL = 1
CHOICE_HOLD = 2

GAME_INTRO = (
    "Welcome to the Tic-Tac-Toe. "
    "Type `help` or `?` to list commands.\n"
)

GAME_RULES = (
    'Game Rules:',
    '1. Rule one.',
    '2. Rule one.',
    '3. Rule one.',
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
