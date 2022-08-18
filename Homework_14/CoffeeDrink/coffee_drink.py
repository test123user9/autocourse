from abc import ABC, abstractmethod


class CoffeeDrink(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, param):
        pass

    @property
    @abstractmethod
    def drink_name(self):
        pass

