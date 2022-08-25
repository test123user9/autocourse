from datetime import date
import pytest

from Homework_16.Human.Staff.SubStaff.head_teacher import HeadTeacher
from Homework_16.Human.gender import Gender


@pytest.fixture
def head_teacher():
    return HeadTeacher('Saniya', 'Childs', date(1980, 5, 23), Gender.FEMALE, 30000)


def test_head_teacher_name(head_teacher):
    name = head_teacher.name
    assert name == 'Saniya', \
        f'Wrong {head_teacher.position} name. \
        Should be {head_teacher.name}'


def test_head_teacher_surname(head_teacher):
    surname = head_teacher.surname
    assert surname == 'Childs', \
        f'Wrong {head_teacher.position} surname. \
        Should be {head_teacher.surname}'

def test_head_teacher_age(head_teacher):
    age = head_teacher.age
    assert age == 42, \
        f'Wrong {head_teacher.position} age. \
        Should be {head_teacher.age}'


