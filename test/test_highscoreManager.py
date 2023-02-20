"""Here is a docstring."""
import unittest
from src.highscoreManager import HighscoreManager 
from src.config import config
import os

class Test_highscoreManager(unittest.TestCase):
    """Docs for public class."""

    def test_highscore_container_type(self):
        """Highscore container should be a dictionary."""
        highscore_manager = HighscoreManager()
        highscores_type = type(highscore_manager._highscores)
        self.assertTrue(highscores_type is dict)

    def test_clear_all(self):
        highscore_manager = HighscoreManager()
        highscore_manager.set_score_by_name('a', 1)
        highscore_manager.set_score_by_name('b', 2)

        a_score = highscore_manager.get_score_by_name('a')
        b_score = highscore_manager.get_score_by_name('b')

        self.assertTrue(a_score, 1)
        self.assertTrue(b_score, 2)

        highscore_manager._clear_all()

        a_score = highscore_manager.get_score_by_name('a')
        b_score = highscore_manager.get_score_by_name('b')

        self.assertIsNone(a_score)
        self.assertIsNone(b_score)

    def test_set_score_by_name(self):
        highscore_manager = HighscoreManager()

        highscore_manager.set_score_by_name('Obunga', 1234)
        currentScore = highscore_manager.get_score_by_name('Obunga')
        self.assertEqual(currentScore, 1234)

        highscore_manager.set_score_by_name('Obunga', 4444)
        currentScore = highscore_manager.get_score_by_name('Obunga')
        self.assertEqual(currentScore, 4444)

        highscore_manager.set_score_by_name('Obunga', -123)
        currentScore = highscore_manager.get_score_by_name('Obunga')
        self.assertEqual(currentScore, 0)

        highscore_manager.set_score_by_name('Obunga', 123)
        currentScore = highscore_manager.get_score_by_name('Obunga')
        self.assertEqual(currentScore, 123)

        highscore_manager.set_score_by_name('Pleb', 123)
        currentScore = highscore_manager.get_score_by_name('Pleb')
        self.assertEqual(currentScore, 123)
    
    def test_get_score_by_name(self):
        highscore_manager = HighscoreManager()
        highscore_manager.set_score_by_name('Obunga', 123)
        highscore_manager.set_score_by_name('Pleb', 3321)
        highscore_manager.set_score_by_name('Jimmy', 12)
        highscore_manager.set_score_by_name('Frodo', 32)
        highscore_manager.set_score_by_name('Smiegol', -32)

        obunga_score = highscore_manager.get_score_by_name('Obunga')
        pleb_score = highscore_manager.get_score_by_name('Pleb')
        jimmy_score = highscore_manager.get_score_by_name('Jimmy')
        frodo_score = highscore_manager.get_score_by_name('Frodo')
        smiegol_score = highscore_manager.get_score_by_name('Smiegol')
        no_score = highscore_manager.get_score_by_name('Unknown')

        self.assertEqual(obunga_score, 123)
        self.assertEqual(pleb_score, 3321)
        self.assertEqual(jimmy_score, 12)
        self.assertEqual(frodo_score, 32)
        self.assertEqual(smiegol_score, 0)
        self.assertEqual(no_score, None)

    def test_save_scores(self):
        highscore_manager = HighscoreManager()

        highscore_manager.set_score_by_name('Obunga', 123)
        highscore_manager.set_score_by_name('Pleb', 3321)
        highscore_manager.set_score_by_name('Jimmy', 12)
        highscore_manager.set_score_by_name('Frodo', 32)

        obunga_score = highscore_manager.get_score_by_name('Obunga')
        pleb_score = highscore_manager.get_score_by_name('Pleb')
        jimmy_score = highscore_manager.get_score_by_name('Jimmy')
        frodo_score = highscore_manager.get_score_by_name('Frodo')

        self.assertEqual(obunga_score, 123)
        self.assertEqual(pleb_score, 3321)
        self.assertEqual(jimmy_score, 12)
        self.assertEqual(frodo_score, 32)

        highscore_manager.save_scores(config['SCORES_FILE_PATH'])
        self.assertTrue(os.path.exists(config['SCORES_FILE_PATH']))

    def test_load_scores(self):
        highscore_manager = HighscoreManager()

        # should raise FileNotFoundError when the file doesn't exist.
        if not os.path.exists(config['SCORES_FILE_PATH']):
            with self.assertRaises(FileNotFoundError):
                highscore_manager.load_scores(config['SCORES_FILE_PATH'])
            return

        highscore_manager.load_scores(config['SCORES_FILE_PATH'])

        obunga_score = highscore_manager.get_score_by_name('Obunga')
        pleb_score = highscore_manager.get_score_by_name('Pleb')
        jimmy_score = highscore_manager.get_score_by_name('Jimmy')
        frodo_score = highscore_manager.get_score_by_name('Frodo')

        self.assertEqual(obunga_score, 123)
        self.assertEqual(pleb_score, 3321)
        self.assertEqual(jimmy_score, 12)
        self.assertEqual(frodo_score, 32)


if __name__ == '__main__':
    unittest.main()
