from datetime import date
import pytest

from Homework_16.Human.Staff.SubStaff.director import Director
from Homework_16.Human.gender import Gender


@pytest.fixture
def director():
    return Director('Brady', 'Christian', date(1975, 11, 14), Gender.OTHER, 50000)


def test_director_name(director):
    name = 'Brady'
    assert name == director.name, \
        f'Wrong {director.position} name. \
        Should be {director.name}'


def test_director_surname(director):
    surname = 'Christian'
    assert surname == director.surname, \
        f'Wrong {director.position} surname. \
        Should be {director.surname}'

def test_director_age(director):
    age = 46
    assert age == director.age, \
        f'Wrong {director.position} age. \
        Should be {director.age}'

