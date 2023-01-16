from controller.controller import Controller
from repository.client_repo import ClientRepo
from repository.drink_repo import DrinkRepo
from repository.cooked_dish_repo import CookedDishRepo
from repository.order_repo import OrderRepo
from datetime import datetime, timedelta


class Console:
    def __init__(self, controller=None):
        self.controller = controller

    # meniul principal
    def main_menu(self):
        def main_menu_ui():
            return """
                0 - Exit
                1 - New order
                2 - Edit data
            """

        while True:
            print(main_menu_ui())
            opt = input('Select = ')

            # deschide meniul pentru a adauga o comanda noua
            if opt == '1':
                self.order_menu()

            # deschide meniul pentru a edita date
            if opt == '2':
                self.edit_menu()

            if opt == '0':
                break

    # meniul de creat comenzi
    def order_menu(self):
        def order_menu_ui():
            return """
                0 - Exit
                1 - Print menu items
                2 - Add item to order
                3 - Add client info
                4 - Finish order
            """

        id = input('Order ID = ')
        client_id = None
        drinks_list = []
        cooked_dishes_list = []

        while True:
            print(order_menu_ui())
            opt = input('Select = ')

            # afiseaza pordusele
            if opt == '1':
                # afiseaza bauturile
                self.controller = Controller(DrinkRepo('repository/data'))
                print(self.controller.repo.read_file('drinks.txt'))

                # afiseaza mancarea
                self.controller = Controller(CookedDishRepo('repository/data'))
                print(self.controller.repo.read_file('cooked_dishes.txt'))

            # adauga produse la comanda
            if opt == '2':
                # adauga produsele noi in 2 liste noi
                new_drinks_list, new_cooked_dishes_list = self.add_items_to_order_menu()
                # adauga noile produse in listele existente pentru a nu se sterge cand se iese din meniu
                drinks_list += new_drinks_list
                cooked_dishes_list += new_cooked_dishes_list

            # adauga id-ul clientului cu comanda
            if opt == '3':
                client_id = self.add_client_info_menu()

            # finalizeaza comanda
            if opt == '4':
                # indica daca nu au fost completate toate datele
                if client_id == None or not drinks_list + cooked_dishes_list:
                    print('Incomplete information:')
                    print('No client info registered') if client_id == None else print('No items added to order')
                else:
                    # calculeaza timpul (cand a fost plasata comanda si cand e gata)
                    time_placed = datetime.now()
                    self.controller = Controller(CookedDishRepo('repository/data'))
                    hours, minutes = self.controller.calculate_time(cooked_dishes_list)
                    expected_time = (time_placed + timedelta(hours=hours, minutes=minutes)).strftime('%H:%M')
                    time_placed = time_placed.strftime('%H:%M')

                    # genereaza comanda
                    self.controller = Controller(OrderRepo('repository/data'))
                    order = self.controller.generate_order(id, client_id, drinks_list, cooked_dishes_list, time_placed,
                                                           expected_time)
                    # afiseaza bonul
                    order.print_check()

            if opt == '0':
                break

    # meniul de adaugat clienti la comanda
    def add_client_info_menu(self):
        def add_client_info_ui():
            return """
                0 - Exit
                1 - Add new client to order
                2 - Add existing client to order
            """

        self.controller = Controller(ClientRepo('repository/data'))
        while True:
            print(add_client_info_ui())
            opt = input('Select = ')

            # adauga informatiile unui client nou la comanda si returneaza id-ul lui
            if opt == '1':
                id = input('ID = ')
                name = input('Name = ')
                address = input('Address = ')
                # salveaza informatiile in fisier
                self.controller.add_client(id, name, address)
                return id

            # returneaza id-ul unui client existent, cautandu-l dupa nume sau adresa
            if opt == '2':
                client_info = input('Enter client info (name/address) = ')
                # id este None daca nu se gaseste clientul sau exista mai multi cu aceleasi informatii
                id, nr_app = self.controller.search_client_id(client_info)
                if nr_app == 1:
                    return id
                elif nr_app == 0:
                    print('No client with such info exists, try again.')
                else:
                    print(f'{nr_app} clients with this info exist, try again with more secific info.')

            if opt == '0':
                break

    # meniul de adaugat produse la comanda
    # returneaza si listele cu id-urile produselor comandate
    def add_items_to_order_menu(self):
        def add_items_to_order_ui():
            return """
                0 - Exit
                1 - Add drinks
                2 - Add cooked dishes
            """

        drinks_list = []
        cooked_dishes_list = []
        while True:
            print(add_items_to_order_ui())
            opt = input('Select = ')

            # adauga id-ul unei bauturi in lista
            if opt == '1':
                self.controller = Controller(DrinkRepo('repository/data'))
                id = input('Enter the ID = ')
                if self.controller.search_item(id, opt):
                    drinks_list.append(id)
                else:
                    print(f'The item with the ID:{id} does not exist')

            # adauga id-ul unui fel de mancare in lista
            if opt == '2':
                self.controller = Controller(CookedDishRepo('repository/data'))
                id = input('Enter the ID = ')
                if self.controller.search_item(id, opt):
                    cooked_dishes_list.append(id)
                else:
                    print(f'The item with the ID:{id} does not exist')

            if opt == '0':
                break

        return drinks_list, cooked_dishes_list

    # meniul de ales ce sa fie editat
    def edit_menu(self):
        def edit_menu_ui():
            return """
                0 - Exit
                1 - Edit drinks
                2 - Edit cooked dishes
                3 - Edit clients
            """

        while True:
            print(edit_menu_ui())
            opt = input('Select = ')

            # se editeaza bauturile
            if opt == '1':
                self.edit_drinks_menu()

            # se editeaza mancarea
            if opt == '2':
                self.edit_cooked_dishes_menu()

            # se editeaza clientii
            if opt == '3':
                self.edit_client_menu()

            if opt == '0':
                break

    # meniul de editat bauturile
    def edit_drinks_menu(self):
        def edit_drinks_ui():
            return """
                0 - Exit
                1 - Add drink
                2 - Print drinks
                3 - Edit drink
                4 - Remove drink
            """

        self.controller = Controller(DrinkRepo('repository/data'))
        while True:
            print(edit_drinks_ui())
            opt = input('Select = ')

            # adauga o bautura noua in fisier
            if opt == '1':
                id = input('ID = ')
                name = input('Name = ')
                portion_size = input('Portion size = ')
                price = input('Price = ')
                alcohol_content = input('Alcohol content = ')
                self.controller.add_drink(id, name, portion_size, price, alcohol_content)

            # afiseaza bauturile din fisier
            if opt == '2':
                print(self.controller.repo.read_file('drinks.txt'))

            # editeaza o bautura, dupa id
            if opt == '3':
                edit_id = input('Enter the ID of the drink you want to edit = ')
                self.controller.edit_drink(edit_id)

            # sterge o bautura din lista, dupa id
            if opt == '4':
                delete_id = input('Enter the ID of the drink you want to delete = ')
                self.controller.delete_entry(delete_id, 'drinks.txt')

            if opt == '0':
                break

    # meniul de editat mancarea
    def edit_cooked_dishes_menu(self):
        def edit_cooked_dishes_ui():
            return """
                0 - Exit
                1 - Add cooked dish
                2 - Print cooked dishes
                3 - Edit cooked dish
                4 - Remove cooked dish
            """

        self.controller = Controller(CookedDishRepo('repository/data'))
        while True:
            print(edit_cooked_dishes_ui())
            opt = input('Select = ')

            # adauga un fel nou de mancare in fisier
            if opt == '1':
                id = input('ID = ')
                name = input('Name = ')
                portion_size = input('Portion size = ')
                price = input('Price = ')
                prep_time = input('Preparation time = ')
                self.controller.add_cooked_dish(id, name, portion_size, price, prep_time)

            # afiseaza felurile de mancare din fisier
            if opt == '2':
                print(self.controller.repo.read_file('cooked_dishes.txt'))

            # editeaza un fel de mancare, dupa id
            if opt == '3':
                edit_id = input('Enter the ID of the cooked dish you want to edit = ')
                self.controller.edit_cooked_dish(edit_id)

            # sterge un fel de mancare, dupa id
            if opt == '4':
                delete_id = input('Enter the ID of the cooked dish you want to delete = ')
                self.controller.delete_entry(delete_id, 'cooked_dishes.txt')

            if opt == '0':
                break

    # meniul de editat clienti
    def edit_client_menu(self):
        def edit_client_ui():
            return """
                0 - Exit
                1 - Add client
                2 - Print clients
                3 - Edit client
                4 - Remove client
            """

        self.controller = Controller(ClientRepo('repository/data'))
        while True:
            print(edit_client_ui())
            opt = input('Select = ')

            # adauga un client nou in fisier
            if opt == '1':
                id = input('ID = ')
                name = input('Name = ')
                address = input('Address = ')
                self.controller.add_client(id, name, address)

            # afiseaza clientii din fisier
            if opt == '2':
                print(self.controller.repo.read_file('clients.txt'))

            # editeaza un client, dupa id
            if opt == '3':
                # se citesc noile date
                print('Enter new info:')
                new_name = input('New name = ')
                new_address = input('New address = ')

                edit_id = input('Enter the ID of the client you want to edit = ')
                self.controller.edit_client(edit_id, new_name, new_address)

            # sterge un client, dupa id
            if opt == '4':
                delete_id = input('Enter the ID of the client you want to delete = ')
                self.controller.delete_entry(delete_id, 'clients.txt')

            if opt == '0':
                break
