from Homework_14.CoffeeDrink.CoffeeDrinks.black_coffee import BlackCoffee
from Homework_14.CoffeeDrink.CoffeeDrinks.cappuccino import Cappuccino
from Homework_14.CoffeeDrink.CoffeeDrinks.espresso import Espresso
from Homework_14.CoffeeDrink.CoffeeDrinks.latte import Latte
from Homework_14.coffee_machine import CoffeeMachine

coffee_machine = CoffeeMachine()

print('Espresso order')
espresso = Espresso()
espresso_with_toppings = espresso.drink_with_toppings
money = 80
print(f'Credit: ${money}')
coffee_machine.order_drink(espresso_with_toppings, money)

print()
print('Americano order')
americano = BlackCoffee()
americano_with_toppings = americano.drink_with_toppings
money = 100
print(f'Credit: ${money}')
coffee_machine.order_drink(americano_with_toppings, money)

print()
print('Latte order')
latte = Latte()
latte_with_toppings = latte.drink_with_toppings
money = 200
print(f'Credit: ${money}')
coffee_machine.order_drink(latte_with_toppings, money)

print()
print('Cappuccino order')
cappuccino = Cappuccino()
cappuccino_with_toppings = cappuccino.drink_with_toppings
money = 300
print(f'Credit: ${money}')
coffee_machine.order_drink(cappuccino_with_toppings, money)