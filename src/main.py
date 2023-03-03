"""Module docstring."""

import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from console import Console


def main():
    """Initialize terminal loop."""
    Console().cmdloop()


if __name__ == '__main__':
    main()
