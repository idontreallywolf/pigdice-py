"""Contains configurations."""

import pathlib

MAX_PLAYERS = 2

CHOICE_ROLL = 1
CHOICE_HOLD = 2

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

GAMEPLAY_CHOICE_HOLD = 1
GAMEPLAY_CHOICE_ROLL = 2
GAMEPLAY_CHOICE_CHEAT = 3
GAMEPLAY_CHOICE_END_GAME = 4
GAMEPLAY_CHOICE_CHANGE_NAME = 5

GAMEPLAY_OPTIONS_MENU = (
    (GAMEPLAY_CHOICE_HOLD, 'HOLD', '✊'),
    (GAMEPLAY_CHOICE_ROLL, 'ROLL', '🎲'),
    (GAMEPLAY_CHOICE_CHEAT, 'CHEAT', '⏩'),
    (GAMEPLAY_CHOICE_END_GAME, 'END GAME', '❌'),
    (GAMEPLAY_CHOICE_CHANGE_NAME, 'CHANGE NAME', '✏️')
)

GAME_TURN_WON = 1
GAME_TURN_LOST = 2
GAME_TURN_NEUTRAL = 3

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
