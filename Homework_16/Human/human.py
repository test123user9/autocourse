from dataclasses import dataclass
from datetime import date

from Homework_15.Human.gender import Gender


@dataclass
class Human:
    name: str
    surname: str
    __birth_date: date
    gender: Gender

    @property
    def age(self) -> int:
        """
        Counts class object's age

        :return: counted age in type int
        """
        return (date.today() - self.birth_date).days // 365

    @property
    def birth_date(self) -> date:
        """
        Displays birth date

        :return: Birth date in type date (yyyy-mm-dd)
        """
        return self.__birth_date

