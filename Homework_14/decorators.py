def syrup(cls):
    def price_with_toppings(self):
        topping_price = 20
        return self.price + topping_price

    cls.price_with_toppings = price_with_toppings
    return cls

def cinnamon(cls):
    def price_with_toppings(self):
        topping_price = 10
        return self.price + topping_price

    cls.price_with_toppings = price_with_toppings
    return cls

def sugar(cls):
    def price_with_toppings(self):
        topping_price = 5
        return self.price + topping_price

    cls.price_with_toppings = price_with_toppings
    return cls

