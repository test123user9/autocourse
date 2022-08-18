from enum import Enum

class Discount(Enum):
    SILVER = 0.5
    GOLD = 1.5
    PREMIUM = 2
    PLATINUM = 3

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


