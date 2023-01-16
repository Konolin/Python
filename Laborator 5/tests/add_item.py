from controller.controller import Controller
from repository.drink_repo import DrinkRepo
from repository.cooked_dish_repo import CookedDishRepo
from os import chdir


# adauga o bautura
def test_add_drink(id, name, portion_size, price, alcohol_content):
    controller = Controller(DrinkRepo('repository/data'))
    controller.add_drink(id, name, portion_size, price, alcohol_content)
    drinks_list = controller.repo.load('drinks.txt')
    drink = drinks_list[-1]

    assert drink.id == id
    assert drink.name == name
    assert drink.portion_size == portion_size
    assert drink.price == price
    assert drink.alcohol_content == alcohol_content


# adauga un tip de mancare
def test_add_cooked_dish(id, name, portion_size, price, prep_time):
    controller = Controller(CookedDishRepo('repository/data'))
    controller.add_cooked_dish(id, name, portion_size, price, prep_time)
    dish_list = controller.repo.load('cooked_dishes.txt')
    dish = dish_list[-1]

    assert dish.id == id
    assert dish.name == name
    assert dish.portion_size == portion_size
    assert dish.price == price
    assert dish.prep_time == prep_time


chdir('../')
test_add_drink(id='10', name='Test', portion_size='123', price='15', alcohol_content='50')
test_add_cooked_dish(id='10', name='Test', portion_size='123', price='15', prep_time='50')
