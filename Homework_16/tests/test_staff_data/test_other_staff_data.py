from datetime import date
import pytest

from Homework_16.Human.Staff.SubStaff.other_staff import OtherStaff
from Homework_16.Human.gender import Gender


@pytest.fixture
def other_staff():
    return OtherStaff('Arda', 'Donald', date(1969, 10, 12), Gender.OTHER, 10000)


def test_other_staff_name(other_staff):
    name = 'Arda'
    assert name == other_staff.name, \
        f'Wrong {other_staff.position} name. \
        Should be {other_staff.name}'


def test_other_staff_surname(other_staff):
    surname = 'Donald'
    assert surname == other_staff.surname, \
        f'Wrong {other_staff.position} surname. \
        Should be {other_staff.surname}'

def test_other_staff_age(other_staff):
    age = 52
    assert age == other_staff.age, \
        f'Wrong {other_staff.position} age. \
        Should be {other_staff.age}'


