from unittest import TestCase, main

from Homework_17.exceptions import IncorrectZeroDiceError, IncorrectNegativeDiceError, IncorrectMoreThanMaxDiceError
from Homework_17.game_class import Game

class GameTests(TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        del self.game

    def test_three_matches(self):
        three_matches = self.game.throw(3, 3, 3)
        self.assertAlmostEqual(three_matches, 300)

    def test_two_matches(self):
        two_matches = self.game.throw(2, 3, 3)
        self.assertAlmostEqual(two_matches, 30)

    def test_no_matches(self):
        no_matches = self.game.throw(2, 3, 1)
        self.assertAlmostEqual(no_matches, 6)

    def test_zero_dice(self):
        with self.assertRaises(IncorrectZeroDiceError):
            self.game.throw(0, 3, 1)

    def test_negative_dice(self):
        with self.assertRaises(IncorrectNegativeDiceError):
            self.game.throw(3, -3, 1)

    def test_exceeding_dice(self):
        with self.assertRaises(IncorrectMoreThanMaxDiceError):
            self.game.throw(16, 3, 1)


if __name__ == '__main__':
    main(argv=[''], verbosity=2, exit=False)
