from modelle.dish import Dish


class Drink(Dish):
    def __init__(self, id, name, portion_size, price, alcohol_content):
        super().__init__(id, name, portion_size, price)
        self.alcohol_content = alcohol_content
