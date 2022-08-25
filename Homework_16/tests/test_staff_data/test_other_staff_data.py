from datetime import date
import pytest

from Homework_16.Human.Staff.SubStaff.other_staff import OtherStaff
from Homework_16.Human.gender import Gender


@pytest.fixture
def other_staff():
    return OtherStaff('Arda', 'Donald', date(1969, 10, 12), Gender.OTHER, 10000)


def test_other_staff_name(other_staff):
    name = other_staff.name
    assert name == 'Arda', \
        f'Wrong {other_staff.position} name. \
        Should be {other_staff.name}'


def test_other_staff_surname(other_staff):
    surname = other_staff.surname
    assert surname == 'Donald', \
        f'Wrong {other_staff.position} surname. \
        Should be {other_staff.surname}'

def test_other_staff_age(other_staff):
    age = other_staff.age
    assert age == 52, \
        f'Wrong {other_staff.position} age. \
        Should be {other_staff.age}'


