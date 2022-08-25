from datetime import date
import pytest

from Homework_16.Human.Staff.SubStaff.student import Student
from Homework_16.Human.gender import Gender


@pytest.fixture
def student():
    return Student('Owain', 'Kline', date(2008, 11, 2), Gender.MALE, 4)


def test_student_name(student):
    name = 'Owain'
    assert name == student.name, \
        f'Wrong {student.position} name. \
        Should be {student.name}'


def test_student_surname(student):
    surname = 'Kline'
    assert surname == student.surname, \
        f'Wrong {student.position} surname. \
        Should be {student.surname}'

def test_student_age(student):
    age = 13
    assert age == student.age, \
        f'Wrong {student.position} age. \
        Should be {student.age}'


