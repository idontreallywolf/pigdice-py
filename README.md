# Pig-Dice Game

## Project Description:
-   The project aims to provide installation and usage instructions for a terminal-based game called “Pig Dice Game”.
-   The game can be played through a Command Line Interface (CLI) and involves players taking turns rolling a single die and accumulating points.
-   The winner is the first player to reach 100 points.
-   The project contains a source folder with all the necessary files to build the terminal application, including a makefile.

## Makefile:
-   The Makefile offers various commands for testing, building, and running the program.
-   Users must install Git Bash on their machine and clone the repository using the provided link.
-   Once cloned, users must navigate to the project directory and use the “make venv” command to create a virtual environment.
-   Users must then activate the virtual environment and use the “make install” command to install the necessary modules.
-   The game can be launched using the “make run” command.
-   The Makefile also offers various commands to interact with the game, such as “make test”, “make pyreverse” and “make pdoc” .

## Game Options:
-   The game offers five options: exit, help, highscore, rules, and start
-   The “exit” option closes the game, “help” provides instructions on how to play the game, “highscore” displays the current high score, “rules” provides the rules of the game, and “start” begins the game. • Each player can change their name whenever it”s their turn.
-   If the user rolls a 1, they will lose all their acquired options for their current turn, but this can be avoided by finding the cheat code implemented in the game or the hold option.
-   After someone has won, the winner will be placed at the top of the highscore board, wich can be viewed from the CLI by typing “highschore”.

### AI Player:
-   The AI player uses a strategy to calculate the player’s expected score for the current turn in the game of Pig Dice.
-   It looks at the number of points the player has already scored that turn and calculates the probability of getting different numbers on the dice.
-   Based on this calculation, the player can decide whether to roll the dice again or stop and keep the points they have already earned.

## Project Creators:
The project was created by Beilan Guo and Nedim Kanat, who attended the "Methods for Sustainable Programming" course at Kristianstad University.
