from repository.order_repo import OrderRepo
from os import chdir


def test_load_order(order_id):
    repo = OrderRepo('repository/data')

    obj_list = repo.load('orders.txt')
    obj = [o for o in obj_list if o.id == order_id]
    str_obj = repo.convert_to_str(obj)

    assert str_obj[0] == "Order(id=0, client_id=4, drinks_list=['1'], cooked_dishes=[''], total_cost=10 time_placed, time_placed=16:02, expected_time=16:02)"


chdir('../')
test_load_order(order_id='0')
