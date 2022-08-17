from enum import Enum

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
