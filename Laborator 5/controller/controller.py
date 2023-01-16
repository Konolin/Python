from modelle.client import Client
from modelle.cooked_dish import CookedDish
from modelle.drink import Drink
from modelle.order import Order


# reuturneaza indexul pe care se afla 'item' in 'search_list'
def search_index(search_list, item):
    for i, obj in enumerate(search_list):
        if obj == item:
            return i


class Controller:
    def __init__(self, repo):
        self.repo = repo

    # adauga un client nou
    def add_client(self, id, name, address):
        obj_list = self.repo.load('clients.txt')
        obj_list.append(Client(id, name, address))
        self.repo.save(self.repo.convert_to_str(obj_list), 'clients.txt')

    # adauga o bautura noua
    def add_drink(self, id, name, portion_size, price, alcohol_content):
        obj_list = self.repo.load('drinks.txt')
        obj_list.append(Drink(id, name, portion_size, price, alcohol_content))
        self.repo.save(self.repo.convert_to_str(obj_list), 'drinks.txt')

    # adauga un fel de mancare nou
    def add_cooked_dish(self, id, name, portion_size, price, prep_time):
        obj_list = self.repo.load('cooked_dishes.txt')
        obj_list.append(CookedDish(id, name, portion_size, price, prep_time))
        self.repo.save(self.repo.convert_to_str(obj_list), 'cooked_dishes.txt')

    # editeaza un client
    def edit_client(self, edit_id, new_name, new_address):
        # incarca o lista cu clientii existenti, format string
        client_list = self.repo.convert_to_str(self.repo.load('clients.txt'))
        # adauga clientii cu 'id == edi_id' in 'filtered_list'
        filtered_list = list(filter(lambda x: x.split('=')[1].split(',')[0] == edit_id, client_list))

        # daca se gaseste clientul dorit, se editeaza datele
        if filtered_list:
            # se cauta pozitia clientului in 'client_list'
            index = search_index(client_list, filtered_list[0])
            # se inlocuiesc noile date in lista
            client_list[index] = f'Client(id={edit_id}, name={new_name}, address={new_address})'
            # se salveaza schimbarile in fisier
            self.repo.save(client_list, 'clients.txt')
        else:  # in caz ca nu exista clientul cu 'id == edit_id'
            print(f'The client with the ID: {edit_id} does not exist')

    # editeaza o bautura
    def edit_drink(self, edit_id):
        # incarca bauturile existente intr-o lista
        drinks_list = self.repo.convert_to_str(self.repo.load('drinks.txt'))
        # adauga obiectele cautate in 'filtered_list'
        filtered_list = list(filter(lambda x: x.split('=')[1].split(',')[0] == edit_id, drinks_list))

        # daca se gaseste bautura dorit, se editeaza datele
        if filtered_list:
            # se citesc datele noi
            print('Enter new info:')
            new_name = input('New name = ')
            new_portion_size = input('New portion size = ')
            new_price = input('New price = ')
            new_alcohol_content = input('New alcohol content = ')

            # se cauta pozitia bauturii in 'drinks_list'
            index = search_index(drinks_list, filtered_list[0])
            # se inlocuiesc noile date
            drinks_list[
                index] = f'Drink(id={edit_id}, name={new_name}, portion_size={new_portion_size}, price={new_price}, alcohool_content={new_alcohol_content})'
            # se salveaza modificarile
            self.repo.save(drinks_list, 'drinks.txt')
        else:  # in caz ca nu exista bautura cautata
            print(f'The drink with the ID: {edit_id} does not exist')

    # editeaza un fel de mancare
    def edit_cooked_dish(self, edit_id):
        # se incarca mancarea intr-o lista de string-uri
        cooked_dishes_list = self.repo.convert_to_str(self.repo.load('cooked_dishes.txt'))
        # se adauga manacrea gautata intr-o lista
        filtered_list = list(filter(lambda x: x.split('=')[1].split(',')[0] == edit_id, cooked_dishes_list))

        # daca exista manacrea cautata se editeaza
        if filtered_list:
            # se introduc datele noi
            print('Enter new info:')
            new_name = input('New name = ')
            new_portion_size = input('New portion size = ')
            new_price = input('New price = ')
            new_prep_time = input('New preparation time = ')

            # se cauta pozitia mancarii in 'cooked_dishes_list'
            index = search_index(cooked_dishes_list, filtered_list[0])
            # se inlocuiesc datele
            cooked_dishes_list[
                index] = f'CookedDish(id={edit_id}, name={new_name}, portion_size={new_portion_size}, price={new_price}, prep_time={new_prep_time})'
            # se salveaza informatiile
            self.repo.save(cooked_dishes_list, 'cooked_dishes.txt')
        else:  # in caz ca nu exista mancarea cautata
            print(f'The cooked dish with the ID: {edit_id} does not exist')

    # sterge un client/ o bautura/ un fel de mancare
    def delete_entry(self, delete_id, file):
        # se incarca o lista cu elementele fisierului
        entry_list = self.repo.convert_to_str(self.repo.load(file))
        # adauga elementele cu 'id == edi_id' in 'filtered_list'
        filtered_list = list(filter(lambda x: x.split('=')[1].split(',')[0] == delete_id, entry_list))

        # daca exista un element cu 'id == delete_id', atunci se sterge
        if filtered_list:
            entry_list.remove(filtered_list[0])
            self.repo.save(entry_list, file)
        else:  # in caz ca nu exista acel element
            # transforma 'file' in tipul de element, pentru a se putea afisa
            item = file[:-6].replace("_", " ") if file == 'cooked_dishes.txt' else file[:-5]
            print(f'The {item} with the ID: {delete_id} does not exist')

    # returneaza un obiect de tip 'order' si il salveaza in fisier
    def generate_order(self, id, client_id, drinks_list, cooked_dishes_list, time_placed, expected_time):
        # creaza obiectul
        order = Order(id, client_id, drinks_list, cooked_dishes_list, time_placed, expected_time)
        # incarca toate comenzile intr-o lista sub format string
        order_list = self.repo.convert_to_str(self.repo.load('orders.txt'))
        # transforma obiectul in string si il adauga in lista
        order_list.append(self.repo.convert_to_str([order])[0])
        # salveaza lista in fisier
        self.repo.save(order_list, 'orders.txt')
        return order

    # returneaza True/False daca exista produsul in fisiere
    # item_type = '1' => drink  /  item_type = '2' => cooked_dish
    def search_item(self, id, item_type):
        if item_type == '1':
            drinks_list = self.repo.convert_to_str(self.repo.load('drinks.txt'))
            filtered_list = list(filter(lambda x: x.split('=')[1].split(',')[0] == id, drinks_list))
        else:
            cooked_dishes_list = self.repo.convert_to_str(self.repo.load('cooked_dishes.txt'))
            filtered_list = list(filter(lambda x: x.split('=')[1].split(',')[0] == id, cooked_dishes_list))
        return True if len(filtered_list) == 1 else False

    # returneaza id si nr_app
    # nr_app = numarul de clienti are contin in nume/adresa 'client_info'
    # id = id-ul clientului  /  id = None daca nu exista clientul sau exista mai multi
    def search_client_id(self, client_info):
        client_info = client_info.lower()
        # se incarca clientii existenti in lista
        client_list = self.repo.convert_to_str(self.repo.load('clients.txt'))

        # se creaza o lista cu clientii care au 'client_info' in nume
        filtered_name_list = list(
            filter(lambda x: client_info in x.split('=')[2].split(',')[0].lower(), client_list))
        # se creaza o lista cu clientii care au 'client_info' in adresa
        filtered_address_list = list(
            filter(lambda x: client_info in x.split('=')[3].split(',')[0].lower(), client_list))
        # se unesc listele
        filtered_list = filtered_address_list + filtered_name_list

        # se elina clientii care apar de mai multe ori ('client_info' apare si in nume si in adresa)
        rez = []
        for el in filtered_list:
            if el not in rez:
                rez.append(el)

        # daca nu exista clienti cu 'client_info'
        if len(rez) == 0:
            return None, 0

        # se transforma lista finala in string si dupa intr-o lista de obiecte
        rez = '\n'.join(rez)
        rez = self.repo.convert_from_str(rez)
        return (rez[0].id, 1) if len(rez) == 1 else (None, len(rez))

    def calculate_time(self, lista):
        # cauta oobiectul cu id-ul corespunzator si il returneaza
        def get_item(id):
            item_list = self.repo.convert_to_str(self.repo.load('cooked_dishes.txt'))
            filtered_list = list(filter(lambda x: x.split('=')[1].split(',')[0] == id, item_list))
            return self.repo.convert_from_str(filtered_list[0])[0]

        # face suma minutelor din 'prep_time'
        minutes = 0
        for id in lista:
            minutes += int(get_item(id).prep_time)

        # transforma minutele in ore si minute
        hours = minutes // 60
        minutes = minutes % 60

        return hours, minutes
