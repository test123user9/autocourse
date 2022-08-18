from Homework_14.CoffeeDrink.coffee_drink import CoffeeDrink
from Homework_14.decorators import sugar, cinnamon, syrup


@syrup
@sugar
@cinnamon
class BlackCoffee(CoffeeDrink):

    def __init__(self):
        self.__drink_name: str = 'Black Coffee'
        self.__price = 75

    def __repr__(self):
        return f'{self.drink_name}(${self.price})'

    @property
    def drink_name(self):
        return self.__drink_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def drink_with_toppings(self):
        print(f'{self.drink_name} with toppings: ${self.price_with_toppings()}')
        return self.price_with_toppings()

if __name__ == '__main__':
    black_coffee = BlackCoffee()
    print(black_coffee)
    black_coffee_with_toppings = black_coffee.price_with_toppings()
    print(black_coffee_with_toppings)

