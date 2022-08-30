from Homework_18.Human.Staff.SubStaff.student import Student
from Homework_18.Human.Staff.SubStaff.teacher import Teacher
from Homework_18.exceptions import TheSameStudentError


class Group:
    def __init__(self, classroom_teacher: Teacher, students: [Student] = None):
        if students is None:
            students = []
        self.__classroom_teacher = classroom_teacher
        self.__students = students

    def __repr__(self) -> str:
        return f'{self.__classroom_teacher}, {self.__students}'

    def __del__(self):
        pass

    @property
    def classroom_teacher(self) -> Teacher:
        return self.__classroom_teacher

    @classroom_teacher.setter
    def classroom_teacher(self, new_class_teacher):
        self.__classroom_teacher = new_class_teacher

    def get_students(self) -> [Student]:
        return self.__students

    def add_student(self, new_student):
        for s in self.__students:
            if new_student == s:
                raise TheSameStudentError('The student already added to the group')
        self.__students.append(new_student)

    def remove_student(self, student):
        self.__students.remove(student)


