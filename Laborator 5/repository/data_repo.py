class DataRepo:
    def __init__(self, file):
        self.file = file  # fisierul care contine fisierele cu date

    # salveaza o lista de obiecte in fisier, fiecare obiect pe cate o linie
    def save(self, obj_list, obj_file):
        with open(f'{self.file}/{obj_file}', 'w') as f:
            for i, obj in enumerate(obj_list):
                f.write(str(obj))
                # opreste scrierea unui rand gol la finalul fisierului
                if i < len(obj_list) - 1:
                    f.write('\n')

    # returneaza o lista de obiecte din fisier
    def load(self, obj_file):
        with open(f'{self.file}/{obj_file}', 'r') as f:
            list_strings = f.read()
        return self.convert_from_str(list_strings)

    # returneaza un string cu tot continutul fisierului
    def read_file(self, obj_file):
        with open(f'{self.file}/{obj_file}', 'r') as f:
            string_file = f.read()
        return string_file

    # scrie un string in fisier
    def write_to_file(self, string_to_file, obj_file):
        with open(f'{self.file}/{obj_file}', 'w') as f:
            f.write(string_to_file)

    def convert_to_str(self, obj_list):
        pass

    def convert_from_str(self, obj_string):
        pass
