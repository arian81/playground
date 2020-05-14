class pizza:
    def __init__(self,toppings):
        self.toppings = toppings
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
ingridients = ["cheese", "onions", "spam", "pineapple"]
if all(pizza.validate_topping(i) for i in ingridients):
    pizza = pizza(ingridients)
print(pizza.toppings)
