import unittest

from unittest.mock import MagicMock, patch

from src.game import Game
from src.highscore_manager import HighscoreManager
from src.player import Player
from src.config import\
    GAME_TURN_NEUTRAL,\
    GAME_TURN_WON,\
    GAME_TURN_LOST

class Test_Game(unittest.TestCase):
    def test_init(self):
        game = Game()
        
        self.assertTrue(type(game.players) is list)
        self.assertEqual(len(game.players), 0)
        self.assertEqual(game.current_player, 0)
        self.assertEqual(game.turn_status, GAME_TURN_NEUTRAL)
        self.assertTrue(type(game.highscore_manager) is HighscoreManager)

    def test_add_player(self):
        game = Game()

        game.add_player('testPlayer')
        new_player: Player = game.players[0]
        self.assertEqual(new_player.get_name(), 'testPlayer')

        game.add_player('testPlayer2')
        new_player: Player = game.players[1]
        self.assertEqual(new_player.get_name(), 'testPlayer2')
    
    def test_get_current_player(self):
        game = Game()

        self.assertIsNone(game.get_current_player())
        game.add_player('testPlayer')

        current_player = game.get_current_player()
        self.assertIsNotNone(current_player)
        self.assertEqual(current_player.get_name(), 'testPlayer')
    
    def test_get_turn_status(self):
        game = Game()

        gts = game.get_turn_status()
        self.assertEqual(gts, GAME_TURN_NEUTRAL)

        game.turn_status = GAME_TURN_LOST
        gts = game.get_turn_status()
        self.assertEqual(gts, GAME_TURN_LOST)

        game.turn_status = GAME_TURN_WON
        gts = game.get_turn_status()
        self.assertEqual(gts, GAME_TURN_WON)

    def test_set_turn_status(self):
        game = Game()

        gts = game.get_turn_status()
        self.assertEqual(gts, GAME_TURN_NEUTRAL)

        game.set_turn_status(GAME_TURN_WON)
        gts = game.get_turn_status()
        self.assertEqual(gts, GAME_TURN_WON)

        game.set_turn_status(GAME_TURN_LOST)
        gts = game.get_turn_status()
        self.assertEqual(gts, GAME_TURN_LOST)

        game.set_turn_status(GAME_TURN_NEUTRAL)
        gts = game.get_turn_status()
        self.assertEqual(gts, GAME_TURN_NEUTRAL)
    
    @patch('src.dice.Dice.roll')
    def test_roll_loss(self, mock_dice_roll: MagicMock):
        game = Game()

        # fake the return value of Dice.roll method.
        mock_dice_roll.return_value = 1

        game.add_player('player_one')
        game.add_player('player_two')

        # Player should "roll a 1" and lose.
        game.roll()

        self.assertEqual(game.get_turn_status(), GAME_TURN_LOST)
        current_player = game.get_current_player()
        temp_score = current_player.get_temporary_score()
        self.assertEqual(temp_score, 0)

    @patch('src.dice.Dice.roll')
    def test_roll_win(self, mock_dice_roll: MagicMock):
        game = Game()

        # fake the return value of Dice.roll method.
        mock_dice_roll.return_value = 100

        game.add_player('player_one')
        game.roll()

        self.assertEqual(game.get_turn_status(), GAME_TURN_WON)

    @patch('src.dice.Dice.roll')
    def test_roll_neutral(self, mock_dice_roll: MagicMock):
        game = Game()

        # fake the return value of Dice.roll method.
        mock_dice_roll.return_value = 2

        game.add_player('player_one')
        game.roll()

        self.assertEqual(game.get_turn_status(), GAME_TURN_NEUTRAL)

    def test_cheat(self):
        game = Game()
        game.add_player('player_one')
        game.cheat()

        current_player = game.get_current_player()
        self.assertEqual(current_player.get_score(), 100)
        self.assertEqual(game.get_turn_status(), GAME_TURN_WON)

    def test_change_name(self):
        game = Game()
        game.add_player('player_one')
        game.change_name('p1_new_name')
        
        current_player = game.get_current_player()
        self.assertEqual(current_player.get_name(), 'p1_new_name')

    def test_quit(self):
        game = Game()
        game.add_player('p1')
        game.add_player('p2')

        self.assertEqual(len(game.players), 2)

        self.assertEqual(game.current_player, 0)
        game.change_turn()
        self.assertEqual(game.current_player, 1)

        game.quit()
        self.assertEqual(len(game.players), 0)
        self.assertEqual(game.current_player, 0)

if __name__ == '__main__':
    unittest.main()
