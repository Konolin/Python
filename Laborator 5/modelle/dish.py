from modelle.identifiable import Identifiable


class Dish(Identifiable):
    def __init__(self, id, name, portion_size, price):
        super().__init__(id)
        self.name = name
        self.portion_size = portion_size
        self.price = price
