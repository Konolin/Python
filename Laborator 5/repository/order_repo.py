from repository.data_repo import DataRepo
from modelle.order import Order


class OrderRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    # transforma o lista de obiecte intr-o lista de string-uri
    def convert_to_str(self, obj_list):
        # transforma un obiect intr-un string
        def str_obj(o):
            return f'Order(id={o.id}, client_id={o.client_id}, drinks_list={o.drinks_list}, cooked_dishes={o.cooked_dishes_list}, total_cost={o.total_cost}, time_placed={o.time_placed}, expected_time={o.expected_time})'

        return list(map(str_obj, obj_list))

    # transforma un string intr-o lista de obiecte
    def convert_from_str(self, string_file):
        # transforma un string intr-un obiect
        def create_order(element):
            element = element[:-1]  # elimina ultima ')'
            attributes = element.split('=')

            # extrage valorile de dupa '='
            id = attributes[1].split(',')[0]
            client_id = attributes[2].split(',')[0]

            # creaza o lista cu valorile dintre '[]'
            drinks_list = [s.strip("[' ]") for s in attributes[3].split(',')[:-1]]
            cooked_dishes_list = [s.strip("[' ]") for s in attributes[4].split(',')[:-1]]

            # extrage valorile de dupa '='
            total_cost = attributes[5].split(',')[0]
            time_placed = attributes[6].split(',')[0]
            expected_time = attributes[7].split(',')[0]

            return Order(id, client_id, drinks_list, cooked_dishes_list, time_placed, expected_time, total_cost)

        string_list = string_file.split('\n')
        return list(map(create_order, string_list))
