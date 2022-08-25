from datetime import date
import pytest

from Homework_16.Human.Staff.SubStaff.teacher import Teacher
from Homework_16.Human.gender import Gender


@pytest.fixture
def teacher():
    return Teacher('Keanu', 'Zimmerman', date(1995, 9, 12), Gender.MALE, 25000)


def test_teacher_name(teacher):
    name = 'Keanu'
    assert name == teacher.name, \
        f'Wrong {teacher.position} name. \
        Should be {teacher.name}'


def test_teacher_surname(teacher):
    surname = 'Zimmerman'
    assert surname == teacher.surname, \
        f'Wrong {teacher.position} surname. \
        Should be {teacher.surname}'

def test_teacher_age(teacher):
    age = 26
    assert age == teacher.age, \
        f'Wrong {teacher.position} age. \
        Should be {teacher.age}'


