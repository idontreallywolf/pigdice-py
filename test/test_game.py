"""Contains Tests for Game class."""

import unittest

from unittest.mock import MagicMock, patch

from src.game import Game
from src.highscore_manager import HighscoreManager
from src.player import Player
from src.config import\
    GAME_TURN_NEUTRAL,\
    GAME_TURN_WON,\
    GAME_TURN_LOST,\
    DICE_SIDES,\
    GAMEPLAY_CHOICE_HOLD,\
    GAMEPLAY_CHOICE_ROLL,\
    GAMEPLAY_CHOICE_CHEAT


class Test_Game(unittest.TestCase):
    """Tests for Game class."""

    def test_init(self):
        """Test initial game state."""
        game = Game()

        self.assertTrue(type(game.players) is list)
        self.assertEqual(len(game.players), 0)
        self.assertEqual(game.current_player, 0)
        self.assertEqual(game.last_roll, 0)
        self.assertEqual(game.turn_status, GAME_TURN_NEUTRAL)
        self.assertTrue(type(game.highscore_manager) is HighscoreManager)

    def test_add_player(self):
        """
        Test Game.add_player method.

        Players that were created should be retrieved in the same order.
        """
        game = Game()

        game.add_player('testPlayer')
        new_player: Player = game.players[0]
        self.assertEqual(new_player.get_name(), 'testPlayer')

        game.add_player('testPlayer2')
        new_player: Player = game.players[1]
        self.assertEqual(new_player.get_name(), 'testPlayer2')

    def test_get_current_player(self):
        """
        Test Game.get_current_player method.

        Should retrieve the player based on `current_player` index.
        """
        game = Game()

        self.assertIsNone(game.get_current_player())
        game.add_player('testPlayer')

        current_player = game.get_current_player()
        self.assertIsNotNone(current_player)
        self.assertEqual(current_player.get_name(), 'testPlayer')

    def test_get_turn_status(self):
        """
        Test game.get_turn_status method.

        Should get the latest updated value for `turn_status`.
        """
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
        """
        Test Game.set_turn_status method.

        Should set the correct value of `turn_status`.
        """
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

    @patch('src.game.Game.roll_dice')
    def test_roll_loss(self, mock_dice_roll: MagicMock):
        """
        Test Game.roll method.

        Mocks Dice.roll to return `1` in order to simulate loss.

        `turn_status` should be set to `GAME_TURN_LOST`.
        """
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

    @patch('src.game.Game.roll_dice')
    def test_roll_win(self, mock_dice_roll: MagicMock):
        """
        Test Game.roll method.

        Mocks Dice.roll to return `100` in order to simulate win.

        `turn_status` should be set to `GAME_TURN_WIN`.
        """
        game = Game()

        # fake the return value of Dice.roll method.
        mock_dice_roll.return_value = 100

        game.add_player('player_one')
        game.roll()

        self.assertEqual(game.get_turn_status(), GAME_TURN_WON)

    @patch('src.game.Game.roll_dice')
    def test_roll_neutral(self, mock_dice_roll: MagicMock):
        """
        Test Game.roll method.

        Mocks Dice.roll to return `2` in order to simulate a neutral turn.

        `turn_status` should be set to `GAME_TURN_NEUTRAL`.
        """
        game = Game()

        # fake the return value of Dice.roll method.
        mock_dice_roll.return_value = 2

        game.add_player('player_one')
        game.roll()

        self.assertEqual(game.get_turn_status(), GAME_TURN_NEUTRAL)

    def test_cheat(self):
        """
        Test Game.cheat method.

        Player should have `100` in score and
        `turn_status` should be set to `GAME_TURN_WON`.
        """
        game = Game()
        game.add_player('player_one')
        game.cheat()

        current_player = game.get_current_player()
        self.assertEqual(current_player.get_score(), 100)
        self.assertEqual(game.get_turn_status(), GAME_TURN_WON)

    def test_change_name(self):
        """
        Test Game.change_name.

        Should change player's name `player_one` to `p1_new_name`.
        """
        game = Game()
        game.add_player('player_one')
        game.change_name('p1_new_name')

        current_player = game.get_current_player()
        self.assertEqual(current_player.get_name(), 'p1_new_name')

    def test_quit(self):
        """
        Test Game.quit method.

        Should reset game's state.
        """
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

    def test_get_last_roll(self):
        """
        Test Game.get_last_roll method.

        Should return 0, 1, 0 in order.
        """
        game = Game()

        self.assertEqual(game.get_last_roll(), 0)
        game.last_roll = 1
        self.assertEqual(game.get_last_roll(), 1)
        game.last_roll = 0
        self.assertEqual(game.get_last_roll(), 0)

    def test_set_last_roll(self):
        """
        Test Game.set_last_roll method.

        Should set last roll to 1, 0 in order.
        """
        game = Game()

        self.assertEqual(game.last_roll, 0)
        game.set_last_roll(1)
        self.assertEqual(game.last_roll, 1)
        game.set_last_roll(0)
        self.assertEqual(game.last_roll, 0)

    def test_roll_single(self):
        """Test value type and valid value."""
        game = Game()   
        result = game.roll_dice()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, DICE_SIDES)
        self.assertTrue(1 <= result <= 6)

    def test_parse_choice_roll(self):
        """Test parse_choice method with roll choice."""
        game = Game()
        game.roll = MagicMock()
        game.parse_choice(GAMEPLAY_CHOICE_ROLL)
        game.roll.assert_called_once()

    def test_parse_choice_hold(self):
        """Test parse_choice method with roll choice."""
        game = Game()
        game.hold = MagicMock()
        game.parse_choice(GAMEPLAY_CHOICE_HOLD)
        game.hold.assert_called_once()

    def test_parse_choice_cheat(self):
        """Test parse_choice method with roll choice."""
        game = Game()
        game.cheat = MagicMock()
        game.parse_choice(GAMEPLAY_CHOICE_CHEAT)
        game.cheat.assert_called_once()

    def test_load(self):
        """Test load method."""
        game = Game()
        game.highscore_manager.load_scores = MagicMock()
        game.load()
        game.highscore_manager.load_scores.assert_called_once()

    def test_save(self):
        """Test save method."""
        game = Game()
        game.highscore_manager.save_scores = MagicMock()
        game.save()
        game.highscore_manager.save_scores.assert_called_once()

    def test_change_turn(self):
        """Test change_turn method."""
        game = Game()
        self.assertEqual(game.current_player, 0)
        game.change_turn()
        self.assertEqual(game.current_player, 1)
        game.change_turn()
        self.assertEqual(game.current_player, 0)


if __name__ == '__main__':
    unittest.main()
