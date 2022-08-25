from datetime import date
import pytest

from Homework_16.Human.Staff.SubStaff.director import Director
from Homework_16.Human.gender import Gender


@pytest.fixture
def director():
    return Director('Brady', 'Christian', date(1975, 11, 14), Gender.OTHER, 50000)


def test_director_name(director):
    name = director.name
    assert name == 'Brady', \
        f'Wrong {director.position} name. \
        Should be {director.name}'


def test_director_surname(director):
    surname = director.surname
    assert surname == 'Christian', \
        f'Wrong {director.position} surname. \
        Should be {director.surname}'

def test_director_age(director):
    age = director.age
    assert age == 46, \
        f'Wrong {director.position} age. \
        Should be {director.age}'

