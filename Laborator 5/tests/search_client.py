from controller.controller import Controller
from repository.client_repo import ClientRepo
from os import chdir


def test_search_client(client_info):
    controller = Controller(ClientRepo('repository/data'))
    # id = id-ul clientului cautat
    # nr_app = numarul de clienti care contin 'client_info'
    # daca 'nr_app' > 1 => id = None
    id, nr_app = controller.search_client_id(client_info)
    assert id == '1'
    assert nr_app == 1


chdir('../')
test_search_client(client_info='Stef')
