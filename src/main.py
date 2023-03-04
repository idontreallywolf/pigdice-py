"""Main module is responsible for starting the process.

Calls Console's cmdloop method in order to start the command line input process.
"""

import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from console import Console


def main():
    """Start console loop."""
    Console().cmdloop()


if __name__ == '__main__':
    main()
