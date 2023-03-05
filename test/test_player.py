"""Test module for Player class."""
import unittest
from src.player import Player


class Test_Player(unittest.TestCase):
    """Test Player."""

    def test_init_player(self):
        """
        Test initial state of Player.

        :`_name` should be `Smiegol`
        :`_score` should be `0`
        :`_temporary_score` should be `0`
        :`_is_ai` should be `False`
        """
        player = Player('Smiegol')
        self.assertEqual(player._name, 'Smiegol')
        self.assertEqual(player._score, 0)
        self.assertEqual(player._temporary_score, 0)
        self.assertFalse(player._is_ai)

    def test_init_AI(self):
        """
        Test initial state of Player.

        :`_name` should be `AI`
        :`_score` should be `0`
        :`_temporary_score` should be `0`
        :`_is_ai` should be `True`
        """
        player = Player('AI')
        self.assertEqual(player._name, 'AI')
        self.assertEqual(player._score, 0)
        self.assertEqual(player._temporary_score, 0)
        self.assertTrue(player._is_ai)

    def test_get_name(self):
        """
        Test Player.get_name method.

        Should return `Jack`.
        """
        player = Player(name='Jack')
        self.assertEqual(player.get_name(), 'Jack')

    def test_set_name(self):
        """
        Test Player.set_name method.

        Should pass for valid names; `'Jack'`, `'Frodo'` and `'Bilbo'`.
        """
        player = Player(name='Jack')
        self.assertEqual(player.get_name(), 'Jack')

        player.set_name('Frodo')
        self.assertEqual(player.get_name(), 'Frodo')

        player.set_name('Bilbo')
        self.assertEqual(player.get_name(), 'Bilbo')

    def test_set_name_invalid(self):
        """
        Test Player.set_name method.

        Shuld raise ValueError for invalid names `''`, `' '`, `'  '`.
        """
        with self.assertRaises(ValueError):
            Player(name='')

        with self.assertRaises(ValueError):
            Player(name=' ')

        with self.assertRaises(ValueError):
            Player(name='  ')

    def test_is_ai_true(self):
        """
        Test Player.is_ai method.

        Should return `True` for player with name `AI`.
        """
        self.assertTrue(Player(name='AI').is_ai())

    def test_is_ai_false(self):
        """
        Test Player.is_ai method.

        Should return `False` for player with name `Jack`.
        """
        self.assertFalse(Player(name='Jack').is_ai())

    def test_get_score(self):
        """
        Test Player.get_score method.

        Should return latest set score.
        """
        player = Player(name='Jack')
        self.assertEqual(player.get_score(), 0)

        player = Player(name='Jack', score=20)
        self.assertEqual(player.get_score(), 20)

        player = Player(name='Jack', score=-5)
        self.assertEqual(player.get_score(), 0)

    def test_set_score(self):
        """
        Test Player.set_score method.

        Should set `_score` as expected.
        """
        player = Player(name='Jack')
        self.assertEqual(player._score, 0)

        player.set_score(5)
        self.assertEqual(player._score, 5)

        player.set_score(-5)
        self.assertEqual(player._score, 0)

    def test_get_temporary_score_initial(self):
        """
        Test Player.get_temporary_score method.

        Should return the initial temporary score, `0`.
        """
        player = Player(name='Jack')
        self.assertEqual(player.get_temporary_score(), 0)

    def test_add_temporary_score(self):
        """
        Test Player.add_temporary_score method.

        Should add temporary scores as expected.
        """
        player = Player(name='Jack')
        self.assertEqual(player._temporary_score, 0)

        player.add_temporary_score(5)
        self.assertEqual(player._temporary_score, 5)

        player.add_temporary_score(5)
        self.assertEqual(player._temporary_score, 10)

        player.add_temporary_score(5)
        self.assertEqual(player._temporary_score, 15)

        player.add_temporary_score(-5)
        self.assertEqual(player._temporary_score, 15)

    def test_reset_temporary_score(self):
        """
        Test Player.reset_temporary_score method.

        Should reset temporary score to `0`.
        """
        player = Player(name='Jack')
        player._temporary_score = 5
        self.assertEqual(player._temporary_score, 5)

        player.reset_temporary_score()
        self.assertEqual(player._temporary_score, 0)

    def test_hold_score(self):
        """
        Test Player.hold_score method.

        Should add temporary score to player's total score.
        """
        player = Player(name='Jack')
        self.assertEqual(player._score, 0)
        self.assertEqual(player._temporary_score, 0)

        player._temporary_score = 5
        player.hold_score()

        self.assertEqual(player._score, 5)

    def test_name_is_valid(self):
        """
        Test Player.name_is_valid method.

        :Should return `False` for invalid names (`''`,`' '`,`'  '`).
        :Should return `True` for valid names
        (`'John'`,`'Frodo'`,`'Gandalf The Gray'`).
        """
        self.assertFalse(Player.name_is_valid(''))
        self.assertFalse(Player.name_is_valid(' '))
        self.assertFalse(Player.name_is_valid('  '))

        self.assertTrue(Player.name_is_valid('John'))
        self.assertTrue(Player.name_is_valid('Frodo'))
        self.assertTrue(Player.name_is_valid('Grandalf The Gray'))
