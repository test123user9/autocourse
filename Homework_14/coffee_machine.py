from Homework_14.discount import Discount
from Homework_14.exceptions import NotEnoughMoney


class CoffeeMachine:

    def order_drink(self, drink, credit):
        discount = 0

        if credit < drink:
            raise NotEnoughMoney(f'Not enough money. You need more ${str(drink - credit)}')

        elif credit in range(50, 100):
            discount = Discount.SILVER.value

        elif credit in range(100, 250):
            discount = Discount.GOLD.value

        elif credit in range(250, 300):
            discount = Discount.PREMIUM.value

        elif credit >= 300:
            discount = Discount.PLATINUM.value

        discounted_value = drink * discount/100
        drink = drink - discounted_value
        print(f'You have {discount}% discount! New coffee price: ${drink}. '
              f'Your change is ${credit - drink} ')




