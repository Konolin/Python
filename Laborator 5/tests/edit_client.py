from controller.controller import Controller
from repository.client_repo import ClientRepo
from os import chdir


def test_edit_client(edit_id, new_name, new_address):
    controller = Controller(ClientRepo('repository/data'))
    controller.edit_client(edit_id, new_name, new_address)

    with open('repository/data/clients.txt', 'r') as f:
        clients = f.readlines()
    client = [o for o in clients if f'id={edit_id}' in o]

    assert client[0] == f"Client(id={edit_id}, name={new_name}, address={new_address})\n"


chdir('../')
test_edit_client(edit_id='1', new_name='te', new_address='st')
