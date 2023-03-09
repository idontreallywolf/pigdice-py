# Pig-Dice Game

## Project Description:
The purpose of the project is to learn how to collabrate in a team and exercise writing clean and testable code. 

![pigdice_image](https://github.com/idontreallywolf/pigdice-py/blob/main/data/pigdice.png)

## Installation

### 1. Clone repository
```sh
git clone https://github.com/idontreallywolf/pigdice-py
```

### 2. Navigate to the repository
```sh
cd pigdice-py
```


### 3. Setup virtual env.
```sh
make venv
```

### 4. Activate virutal env.
#### On windows
```sh
.venv/Scripts/activate
```

#### Linux/OSX
```sh
source .venv/bin/activate
```

### 5. Install dependencies
```sh
make install
```

### 6. Run the application
Best performance in PowerShell or Unix Terminal 
```sh
make run
```

## Tests
#### Run all tests
```sh
make test
```

#### Run specific tests
```
make pylint
```
```
make flake8
```
.. or both pylint and flake8:
```sh
make lint
```
#### Unittests
```sh
make unittest
```

#### show coverage report
```sh
make coverage-report
```

## Documentation
#### Generate HTML documentatiion
```sh
make pdoc
```
#### Generate UML diagram (Execute only in Git Bash)
```sh
make pyreverse
```
#### Generate Metrics (Execute only in Git Bash)
```sh
make metrics
```

## Command Options:

The game offers five options: exit, help, highscore, rules, and start

The `exit` option closes the application, `help` provides inforamtion on commands, `highscore` displays the high score table, `rules` provides the rules of the game, and `start` begins the game. 

## About the game
### Game Options:
|Options|Description |
|----|--|
| Hold | Save the turn socre to total score |
| Roll| Roll the dice|
| Cheat | Win the game |
| End Game|  |
| Change Name| Change the current player's name |

### Game description
Each turn, a player repeatedly rolls a dice until either a 1 is rolled or the player decides to "hold":

-   If the player rolls a 1, they score nothing and it becomes the next player's turn.
-   If the player rolls any other number, it is added to their turn total and the player's turn continues.
-   If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

The first player to score 100 or more points wins.
[Wikipedia (Pig dice game)](https://en.wikipedia.org/wiki/Pig_%28dice_game%29)

### AI Player:

The AI player will choose to roll as long as it's current score is less than threshold score. 

## Project Creators:

The project was created by Beilan Guo and Nedim Kanat, who attended the "Methods for Sustainable Programming" course at Kristianstad University.
