from dataclasses import dataclass
from Homework_16.Human.Staff.school_staff import SchoolStaff


@dataclass
class Director(SchoolStaff):
    position = 'Director'



