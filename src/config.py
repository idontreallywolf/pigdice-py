"""Contains configurations."""

import pathlib

PLAYER_X = 'x'
PLAYER_O = 'o'

CHOICE_ROLL = 1
CHOICE_HOLD = 2

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
