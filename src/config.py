import pathlib

current_file_path = pathlib\
    .Path(__file__)\
    .parent.resolve()

config = {}

config['DATA_PATH'] =\
    current_file_path\
    .joinpath('../data/')\
    .resolve()

config['SCORES_FILE_PATH'] = str(\
    config['DATA_PATH']\
    .joinpath('scores.bin')\
    .resolve()
)