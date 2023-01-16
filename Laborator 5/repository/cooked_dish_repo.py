from repository.data_repo import DataRepo
from modelle.cooked_dish import CookedDish


class CookedDishRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    # transforma o lista de obiecte intr-o lista de string-uri
    def convert_to_str(self, obj_list):
        # transforma un obiect intr-un string
        def str_obj(obj):
            return f'CookedDish(id={obj.id}, name={obj.name}, portion_size={obj.portion_size}, price={obj.price}, prep_time={obj.prep_time})'

        return list(map(str_obj, obj_list))

    # transforma un string intr-o lista de obiecte
    def convert_from_str(self, string_file):
        # transforma un string intr-un obiect
        def create_cooked_dish(element):
            # verifica sa nu fie un element gol (in caz ca nu se comanda tipul asta de produs)
            if element:
                element = element[:-1]  # sterge ultima ')'
                attributes = element.split(',')

                # extrage valorile de dupa '='
                id = attributes[0].split('=')[1]
                name = attributes[1].split('=')[1]
                portion_size = attributes[2].split('=')[1]
                price = attributes[3].split('=')[1]
                prep_time = attributes[4].split('=')[1]

                return CookedDish(id, name, portion_size, price, prep_time)

        string_list = string_file.split('\n')
        return list(map(create_cooked_dish, string_list))
