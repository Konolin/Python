from modelle.dish import Dish


class CookedDish(Dish):
    def __init__(self, id, name, portion_size, price, prep_time):
        super().__init__(id, name, portion_size, price)
        self.prep_time = prep_time
