from dataclasses import dataclass
from Homework_18.Human.Staff.school_staff import SchoolStaff


@dataclass
class HeadTeacher(SchoolStaff):
    position = 'Head Teacher'


