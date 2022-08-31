import pytest

from Homework_19.exceptions import IncorrectZeroDiceError, IncorrectNegativeDiceError, IncorrectMoreThanMaxDiceError
from Homework_19.game_class import Game

@pytest.fixture
def game():
    game = Game()
    yield game
    del game

