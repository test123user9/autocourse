from datetime import date
import pytest

from Homework_18.Group.group import Group
from Homework_18.Human.Staff.SubStaff.director import Director
from Homework_18.Human.Staff.SubStaff.head_teacher import HeadTeacher
from Homework_18.Human.Staff.SubStaff.student import Student
from Homework_18.Human.Staff.SubStaff.teacher import Teacher
from Homework_18.Human.gender import Gender
from Homework_18.School.school import School


@pytest.fixture
def school():
    school = School(Director('Jerome', 'Hunter', date(1975, 11, 14), Gender.FEMALE.value, 50000),
                  HeadTeacher('Jarod', 'Mcbride', date(1980, 5, 23), Gender.MALE.value, 30000))
    yield school
    del school

@pytest.fixture
def some_teacher():
    teacher = Teacher('Alisha', 'Figueroa', date(1995, 9, 12), Gender.FEMALE, 25000, 'Math teacher')
    yield teacher
    del teacher

@pytest.fixture
def group():
    group = Group(Teacher('Diya', 'Ali', date(1989, 1, 1), Gender.FEMALE, 20000, 'class teacher'))
    yield group
    del group

@pytest.fixture
def student1():
    student1 = Student('Hallie', 'Pugh', date(2007, 11, 13), Gender.MALE.value, 4)
    yield student1
    del student1

@pytest.fixture
def student2():
    student2 = Student('Christie', 'Douglas', date(2008, 10, 13), Gender.FEMALE.value, 9)
    yield student2
    del student2

@pytest.fixture
def student2_copy():
    student2_copy = Student('Christie', 'Douglas', date(2008, 10, 13), Gender.FEMALE.value, 9)
    yield student2_copy
    del student2_copy

