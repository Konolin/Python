from repository.data_repo import DataRepo
from modelle.drink import Drink


class DrinkRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    # transforma o lista de obiecte intr-o lista de string-uri
    def convert_to_str(self, obj_list):
        # transforma un obiect intr-un string
        def str_obj(obj):
            return f'Drink(id={obj.id}, name={obj.name}, portion_size={obj.portion_size}, price={obj.price}, alcohol_content={obj.alcohol_content})'

        return list(map(str_obj, obj_list))

    # transfroma un string intr-o lista de obiecte
    def convert_from_str(self, string_file):
        # transforma un strin intr-un obiect
        def create_drink(element):
            # verifica sa nu fie un element gol (in caz ca nu se comanda tipul asta de produs)
            if element:
                element = element[:-1]
                attributes = element.split(',')

                # extrage valorile de dupa '='
                id = attributes[0].split('=')[1]
                name = attributes[1].split('=')[1]
                portion_size = attributes[2].split('=')[1]
                price = attributes[3].split('=')[1]
                alcohol_content = attributes[4].split('=')[1]

                return Drink(id, name, portion_size, price, alcohol_content)

        string_list = string_file.split('\n')
        return list(map(create_drink, string_list))
