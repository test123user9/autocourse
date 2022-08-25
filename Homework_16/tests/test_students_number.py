from datetime import date
import pytest

from Homework_16.Group.group import Group
from Homework_16.Human.Staff.SubStaff.student import Student
from Homework_16.Human.Staff.SubStaff.teacher import Teacher
from Homework_16.Human.gender import Gender


@pytest.fixture
def group():
    return Group(Teacher('Diya', 'Ali', date(1989, 1, 1), Gender.FEMALE, 20000, 'class teacher'))

def test_group_students_number(group):
    group.add_student(Student('Christie', 'Douglas', date(2007, 11, 13), Gender.MALE, 4))
    group.add_student(Student('Darci', 'Mejia', date(2009, 1, 3), Gender.MALE, 4))
    group_len = len(group.get_students())
    assert group_len == 2, \
        f'Wrong students number in the group. \
        Should be {group_len}'

def test_group_students_adding_removing_number(group):
    group.add_student(Student('Christie', 'Douglas', date(2007, 11, 13), Gender.MALE, 4))
    group.add_student(Student('Darci', 'Mejia', date(2009, 1, 3), Gender.MALE, 4))
    group.add_student(Student('Pranav', 'Traynor', date(2008, 3, 7), Gender.MALE, 4))
    group.add_student(Student('Delores', 'Robin', date(2008, 7, 9), Gender.MALE, 4))
    group.add_student(Student('Cobie', 'Emerson', date(2007, 9, 12), Gender.MALE, 4))
    group.remove_student(Student('Christie', 'Douglas', date(2007, 11, 13), Gender.MALE, 4))
    group_len = len(group.get_students())
    assert group_len == 4, \
        f'Wrong students number in the group. \
        Should be {group_len}'


