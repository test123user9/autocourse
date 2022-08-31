import pytest

from Homework_19.exceptions import IncorrectZeroDiceError, IncorrectNegativeDiceError, IncorrectMoreThanMaxDiceError


@pytest.mark.parametrize('first, second, third, expected_result', [(3, 3, 3, 300),
                                                                   (2, 3, 3, 30),
                                                                   (2, 3, 1, 6)])
def test_dice_positive_cases(game, first, second, third, expected_result):
    assert game.throw(first, second, third) == expected_result

@pytest.mark.parametrize('first, second, third, exception', [(0, 3, 1, IncorrectZeroDiceError),
                                                             (2, -1, 3, IncorrectNegativeDiceError),
                                                             (7, 3, 1, IncorrectMoreThanMaxDiceError)])
def test_dice_negative_cases(game, first, second, third, exception):
    with pytest.raises(exception):
        _ = game.throw(first, second, third)

