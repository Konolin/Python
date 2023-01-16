from controller.controller import Controller
from repository.order_repo import OrderRepo
from os import chdir


def test_save_order(id, client_id, drinks_list, cooked_dishes_list, time_placed, expected_time):
    controller = Controller(OrderRepo('repository/data'))
    controller.generate_order(id, client_id, drinks_list, cooked_dishes_list, time_placed, expected_time)
    order_list = controller.repo.load('orders.txt')
    order = order_list[-1]

    assert order.id == id
    assert order.client_id == client_id
    assert order.drinks_list == drinks_list
    assert order.cooked_dishes_list == cooked_dishes_list
    assert order.time_placed == time_placed


chdir('../')
test_save_order(id='10', client_id='5', drinks_list=['1', '0'], cooked_dishes_list=['1', '1'], time_placed='10:12',
                expected_time='10:15')
