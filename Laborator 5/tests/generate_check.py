from repository.cooked_dish_repo import CookedDishRepo
from repository.drink_repo import DrinkRepo
from modelle.order import Order
from os import chdir


def test_order(id, client_id, drinks_list, cooked_dishes_list, time_placed, expected_time, total_cost):
    order = Order(id, client_id, drinks_list, cooked_dishes_list, time_placed, expected_time)
    check = f'Order ID = {id}\n' \
            f'Client ID = {client_id}\n' \
            f'============================\n'

    repo = DrinkRepo('repository/data')
    drinks = []
    for id in drinks_list:
        drinks.append(order.get_item(id, 'drinks.txt', repo))
    for drink in drinks:
        check += f'{drink}\n'

    repo = CookedDishRepo('repository/data')
    dishes = []
    for id in cooked_dishes_list:
        drinks.append(order.get_item(id, 'drinks.txt', repo))
    for dish in dishes:
        check += f'{dish}\n'

    check += f'============================\n' \
             f'Total cost = {total_cost}\n' \
             f'Time the order was placed: {time_placed}\n' \
             f'Expected finish time: {expected_time}'
    assert order._Order__string_receipt() == check


chdir('../')
test_order(id='10', client_id='5', drinks_list=['1', '0'], cooked_dishes_list=['1', '1'], time_placed='10:12',
           expected_time='11:12', total_cost='50')
