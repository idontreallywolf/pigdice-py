"""Here is a docstring."""
import unittest
import os

from src.highscore_manager import HighscoreManager
from src.config import TEST_SCORES_FILE_PATH
from src.player import Player
from prettytable import PrettyTable


class Test_highscoreManager(unittest.TestCase):
    """Docs for public class."""

    def test_init(self):
        highscore_manager = HighscoreManager()
        self.assertFalse(highscore_manager._scores_loaded)
        self.assertIsInstance(highscore_manager._highscores, list)
        self.assertIsInstance(highscore_manager.table, PrettyTable)

    def test_get_scores_table(self):
        highscore_manager = HighscoreManager()
        scores_table = highscore_manager.get_scores_table()
        self.assertIsInstance(scores_table, str)

    def test_create_record(self):
        highscore_manager = HighscoreManager()

        p1 = Player('p1')
        p1.set_score(25)

        p2 = Player('p2')
        p2.set_score(44)

        highscore_manager.create_record([p1, p2])
        highscore_records = len(highscore_manager._highscores)
        self.assertTrue(highscore_records > 0)

        first_record = highscore_manager._highscores[0]

        p1_score: int = first_record['p1']
        p2_score: int = first_record['p2']

        self.assertIsNotNone(p1_score)
        self.assertIsNotNone(p2_score)
        self.assertIsInstance(p1_score, int)
        self.assertIsInstance(p2_score, int)
        self.assertEqual(p1_score, 25)
        self.assertEqual(p2_score, 44)

    def test_name_exists_true(self):
        highscore_manager = HighscoreManager()

        p1 = Player('p1')
        p2 = Player('p2')

        highscore_manager.create_record([p1, p2])

        p1_exists = highscore_manager.name_exists('p1')
        p2_exists = highscore_manager.name_exists('p2')

        self.assertTrue(p1_exists)
        self.assertTrue(p2_exists)

    def test_name_exists_false(self):
        highscore_manager = HighscoreManager()

        p1 = Player('p1')
        p2 = Player('p2')

        highscore_manager.create_record([p1, p2])

        p3_exists = highscore_manager.name_exists('p3')
        p4_exists = highscore_manager.name_exists('p4')

        self.assertFalse(p3_exists)
        self.assertFalse(p4_exists)

    def test_change_name_success(self):
        highscore_manager = HighscoreManager()

        p1 = Player('p1')
        p2 = Player('p2')

        highscore_manager.create_record([p1, p2])
        changed = highscore_manager.change_name('p1', 'p1_new')
        self.assertTrue(changed)

    def test_change_name_failure(self):
        highscore_manager = HighscoreManager()

        p1 = Player('p1')
        p2 = Player('p2')

        highscore_manager.create_record([p1, p2])
        changed = highscore_manager.change_name('p1', 'p2')
        self.assertFalse(changed)

    def test_clear_all(self):
        highscore_manager = HighscoreManager()

        p1 = Player('p1')
        p1.set_score(25)

        p2 = Player('p2')
        p2.set_score(44)

        highscore_manager.create_record([p1, p2])
        highscore_manager._clear_all()

        self.assertTrue(len(highscore_manager._highscores) == 0)

    def test_save_scores(self):
        highscore_manager = HighscoreManager()

        p1 = Player('p1')
        p1.set_score(25)

        p2 = Player('p2')
        p2.set_score(44)

        highscore_manager.create_record([p1, p2])
        highscore_manager.save_scores(TEST_SCORES_FILE_PATH)

        self.assertTrue(os.path.exists(TEST_SCORES_FILE_PATH))

    def test_load_scores(self):
        highscore_manager = HighscoreManager()

        # should raise FileNotFoundError when the file doesn't exist.
        if not os.path.exists(TEST_SCORES_FILE_PATH):
            with self.assertRaises(FileNotFoundError):
                highscore_manager.load_scores(TEST_SCORES_FILE_PATH)
            return

        highscore_manager.load_scores(TEST_SCORES_FILE_PATH)

        highscore_records = len(highscore_manager._highscores)
        self.assertTrue(highscore_records > 0)

        first_record = highscore_manager._highscores[0]

        p1_score: int = first_record['p1']
        p2_score: int = first_record['p2']

        self.assertIsNotNone(p1_score)
        self.assertIsNotNone(p2_score)
        self.assertIsInstance(p1_score, int)
        self.assertIsInstance(p2_score, int)
        self.assertEqual(p1_score, 25)
        self.assertEqual(p2_score, 44)


if __name__ == '__main__':
    unittest.main()
