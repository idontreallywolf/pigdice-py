"""Contains utility functions."""

import time

from prettytable import\
    PrettyTable,\
    DOUBLE_BORDER,\
    ALL

from colorama import\
    just_fix_windows_console,\
    Fore, Style

from src.config import GAMEPLAY_OPTIONS_MENU

just_fix_windows_console()


def make_table(title, columns: list[str]) -> PrettyTable:
    """
    Build and return an ASCII table.

    Parameters:
        `columns`: a list of strings containing the names of each column.

    Returns:
        `PrettyTable`: instance of the table.
    """
    table = PrettyTable(columns)

    table.set_style(DOUBLE_BORDER)
    table.header = False
    table.title =\
        Fore.CYAN +\
        (title or "Title") +\
        Style.RESET_ALL
    table.hrules = ALL

    return table


def animate_loading():
    """Display loading animation."""
    animation = [
        '🎲🎲🎲🎲🎲🎲🎲',
        '🐷🎲🎲🎲🎲🎲🎲',
        '🐷🐷🎲🎲🎲🎲🎲',
        '🐷🐷🐷🎲🎲🎲🎲',
        '🐷🐷🐷🐷🎲🎲🎲',
        '🐷🐷🐷🐷🐷🎲🎲',
        '🎲🐷🐷🐷🐷🐷🎲',
        '🎲🎲🐷🐷🐷🐷🐷',
        '🎲🎲🎲🐷🐷🐷🐷',
        '🎲🎲🎲🎲🐷🐷🐷',
        '🎲🎲🎲🎲🎲🐷🐷',
        '🎲🎲🎲🎲🎲🎲🐷'
    ]

    not_complete = True
    i = 0

    while not_complete:
        # \r starts on the same line.
        print(' ', animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1
        if i == 30:
            break


def prepare_options_menu():
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
