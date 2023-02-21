"""Test module for Player class."""
import unittest
from src.player import Player


class Test_Player(unittest.TestCase):
    """Test Player."""

    def test_init(self):
        """Test initial state of Player."""
        player = Player('Smiegol')
        self.assertEqual(player._name, 'Smiegol')
        self.assertEqual(player._score, 0)
        self.assertEqual(player._temporary_score, 0)
        self.assertFalse(player._isAI)

        player = Player('AI')
        self.assertEqual(player._name, 'AI')
        self.assertEqual(player._score, 0)
        self.assertEqual(player._temporary_score, 0)
        self.assertTrue(player._isAI)

    def test_get_name(self):
        """Test get_name."""
        player = Player(name='Jack')
        self.assertEqual(player.get_name(), 'Jack')

    def test_set_name(self):
        """Pass for valid names, 'Jack', 'Frodo' and 'Bilbo'."""
        player = Player(name='Jack')
        self.assertEqual(player.get_name(), 'Jack')

        player.set_name('Frodo')
        self.assertEqual(player.get_name(), 'Frodo')

        player.set_name('Bilbo')
        self.assertEqual(player.get_name(), 'Bilbo')

    def test_set_name_invalid(self):
        """Raise ValueError for invalid names '', ' ', '  '."""
        with self.assertRaises(ValueError):
            Player(name='')

        with self.assertRaises(ValueError):
            Player(name=' ')

        with self.assertRaises(ValueError):
            Player(name='  ')

    def test_isAI(self):
        """Test isAI."""
        player = Player(name='Jack')
        self.assertFalse(player.isAI())

        player = Player(name='AI')
        self.assertTrue(player.isAI())

    def test_get_score(self):
        """Test get score."""
        player = Player(name='Jack')
        self.assertEqual(player.get_score(), 0)

        player = Player(name='Jack', score=20)
        self.assertEqual(player.get_score(), 20)

        player = Player(name='Jack', score=-5)
        self.assertEqual(player.get_score(), 0)

    def test_set_score(self):
        """Test set score."""
        player = Player(name='Jack')
        self.assertEqual(player.get_score(), 0)

        player.set_score(5)
        self.assertEqual(player.get_score(), 5)

        player.set_score(-5)
        self.assertEqual(player.get_score(), 0)

    def test_get_temporary_score_initial(self):
        """Test get score."""
        player = Player(name='Jack')
        self.assertEqual(player.get_temporary_score(), 0)

    def test_add_temporary_score(self):
        """Test get score."""
        player = Player(name='Jack')
        self.assertEqual(player.get_temporary_score(), 0)

        player.add_temporary_score(5)
        self.assertEqual(player.get_temporary_score(), 5)

        player.add_temporary_score(5)
        self.assertEqual(player.get_temporary_score(), 10)

        player.add_temporary_score(5)
        self.assertEqual(player.get_temporary_score(), 15)

        player.add_temporary_score(-5)
        self.assertEqual(player.get_temporary_score(), 15)

    def test_reset_temporary_score(self):
        """Test get score."""
        player = Player(name='Jack')
        player.add_temporary_score(5)
        self.assertEqual(player.get_temporary_score(), 5)

        player.reset_temporary_score()
        self.assertEqual(player.get_temporary_score(), 0)

    def test_hold_score(self):
        """Test hold score."""
        player = Player(name='Jack')
        self.assertEqual(player.get_score(), 0)
        self.assertEqual(player.get_temporary_score(), 0)

        player.add_temporary_score(5)
        player.hold_score()

        self.assertEqual(player.get_score(), 5)

    def test_name_is_valid(self):
        """Test _name_is_valid."""
        self.assertFalse(Player._name_is_valid(''))
        self.assertFalse(Player._name_is_valid(' '))
        self.assertFalse(Player._name_is_valid('  '))

        self.assertTrue(Player._name_is_valid('John'))
        self.assertTrue(Player._name_is_valid('Frodo'))
        self.assertTrue(Player._name_is_valid('Grandalf The Gray'))
