from modelle.identifiable import Identifiable


class Client(Identifiable):
    def __init__(self, id, name, address):
        super().__init__(id)
        self.name = name
        self.address = address
