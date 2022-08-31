from dataclasses import dataclass
from Homework_18.Human.Staff.staff import Staff
from Homework_18.Human.human import Human
from Homework_18.exceptions import InvalidRewardValueError


@dataclass
class SchoolStaff(Staff, Human):
    __reward: int
    __position: str = 'School Staff'

    def __repr__(self) -> str:
        return f'{self.__position}: {self.name} {self.surname}'

    # def __del__(self):
    #     pass

    @property
    def reward(self) -> int:
        return self.__reward

    @property
    def position(self) -> str:
        return self.__position

    @reward.setter
    def reward(self, new_reward):
        if new_reward in range(1, 100000 + 1) and isinstance(new_reward, int):
            self.__reward = new_reward
        else:
            raise InvalidRewardValueError(new_reward)



