import pytest

from Homework_18.exceptions import TheSameStudentError


# fixtures are in the 'conftest.py' file

def test_group_students_adding(school, group, student1, student2):
    school.add_group(group)
    group.add_student(student1)
    assert school.education_cost() == 100000, \
        f'Wrong education cost. \
        Should be {school.education_cost()}'
    group.add_student(student2)
    assert school.education_cost() == 50000, \
        f'Wrong education cost. \
        Should be {school.education_cost()}'


def test_group_students_removing(school, group, student1, student2):
    school.add_group(group)
    group.add_student(student1)
    group.add_student(student2)
    assert school.education_cost() == 50000, \
        f'Wrong education cost. \
        Should be {school.education_cost()}'
    group.remove_student(student1)
    assert school.education_cost() == 100000, \
        f'Wrong education cost. \
        Should be {school.education_cost()}'


def test_count_education_cost(school, group, student1, student2, some_teacher):
    school.add_group(group)
    group.add_student(student1)
    group.add_student(student2)
    assert school.education_cost() == 50000, \
        f'Wrong education cost. \
        Should be {school.education_cost()}'
    school.add_teacher(some_teacher)
    assert school.education_cost() == 62500, \
        f'Wrong education cost. \
        Should be {school.education_cost()}'


def test_adding_the_same_student_instance(group, student1, student2):
    group.add_student(student1)
    group.add_student(student2)
    with pytest.raises(TheSameStudentError):
        _ = group.add_student(student1), \
            f'Exception "TheSameStudentError" hasn\'t been returned \
            after the {student1} instance has been added second time '


def test_adding_the_same_student_copy(group, student1, student2, student2_copy):
    group.add_student(student1)
    group.add_student(student2)
    with pytest.raises(TheSameStudentError):
        _ = group.add_student(student2_copy), \
            f'Exception "TheSameStudentError" hasn\'t been returned \
            after the {student2_copy} has been added while it\'s duplicate of {student2} '
