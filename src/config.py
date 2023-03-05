"""Contains configurations."""

import pathlib

CHOICE_ROLL = 1
CHOICE_HOLD = 2

GAME_RULES = """
Welcome to Pig Dice! 🎉 Be a cute 🐷, score tasty 🍭🍭🍭, and win big! 🏆 Roll on! 🎲🐽
Follow these steps for tasty victory!🍭
1. Roll 🎲 and hope you get a good number.
2. If you roll a 1️⃣, that's a piggy pooper! 🐷💩
2. Get a 5 or 6 and you'll be in candy heaven! 🍭🍭🍭 Roll on, piggy friend! 🎲🐷
3. Got yummy 🍭? Hit 'hold' and munch on! 🤤 Let your piggy pals play! 🎲🐷
4. Keep playing 🎲, collect 🍭, and win at 💯 points to be crowned piggy champ!🐷🏆
5.Hog heaven alert! 🚨 Tie at 💯 points means wild showdown! 🎲🐽
Snacks ready? 🍿 Roll those dice! 🎲 Be the top piggy! 🏆🐷 Oink-tastic fun! 🐽😎
"""

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

TEST_SCORES_FILE_PATH = str(
    DATA_PATH
    .joinpath('scores_test.bin')
    .resolve()
)
