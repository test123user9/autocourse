from datetime import date

# from Homework_18.School.school import School
# from Homework_18.Group.group import Group
from Homework_18.Human.Staff.SubStaff.director import Director
from Homework_18.Human.Staff.SubStaff.head_teacher import HeadTeacher
from Homework_18.Human.Staff.SubStaff.other_staff import OtherStaff
from Homework_18.Human.Staff.SubStaff.student import Student
from Homework_18.Human.Staff.SubStaff.teacher import Teacher
from Homework_18.Human.gender import Gender

if __name__ == '__main__':
    student1 = Student('Name', 'Surname', date(2008, 11, 2), Gender.MALE, 4)
    student2 = Student('Name', 'Surname', date(2008, 11, 2), Gender.MALE, 4)
    print(f'Student 1: {student1.position}, {student1.age}, {student1.gender}. \n'
          f'Student 2: {student2.position}, {student2.age}, {student2.gender}')
    print(student1 == student2)

    class_teacher1 = Teacher('Name', 'Surname', date(1989, 1, 1), Gender.FEMALE, 20000, 'class teacher1')
    class_teacher2 = Teacher('Name', 'Surname', date(1989, 1, 1), Gender.FEMALE, 20000, 'class teacher1')
    print(class_teacher1.gender, class_teacher2.gender)
    print(class_teacher1 == class_teacher2)

    director1 = Director('Name', 'Surname', date(1975, 11, 14), Gender.OTHER, 50000)
    director2 = Director('Name', 'Surname', date(1975, 11, 14), Gender.OTHER, 50000)
    print(director1.gender, director2.gender)
    print(director1 == director2)

    head_teacher1 = HeadTeacher('Name', 'Surname', date(1980, 5, 23), Gender.FEMALE, 30000)
    head_teacher2 = HeadTeacher('Name', 'Surname', date(1980, 5, 23), Gender.FEMALE, 30000)
    print(head_teacher1.gender, head_teacher2.gender)
    print(head_teacher1 == head_teacher2)

    teacher1 = Teacher('Name', 'Surname', date(1995, 9, 12), Gender.MALE, 25000)
    teacher2 = Teacher('Name', 'Surname', date(1995, 9, 12), Gender.MALE, 25000)
    print(teacher1.gender, teacher2.gender)
    print(teacher1 == teacher2)

    other_staff1 = OtherStaff('Name', 'Surname', date(1969, 10, 12), Gender.OTHER, 10000)
    other_staff2 = OtherStaff('Name', 'Surname', date(1969, 10, 12), Gender.OTHER, 10000)
    print(other_staff1.gender, other_staff2.gender)
    print(other_staff1 == other_staff2)

