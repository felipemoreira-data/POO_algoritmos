from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = None):
        self.nome = nome

    @abstractmethod
    def emitir_barulho(self):
        print(f'O animal {self.nome} que é um(a) {self.__class__.__name__} está fazendo barulho!')

class Cachorro(Animal):
    def emitir_barulho(self):
        print(f'{self.nome} está dizendo AUAU')

class Shitzu(Cachorro):
    pass

class Gato(Animal):
    def emitir_barulho(self):
        return super().emitir_barulho()

class Galinha(Animal):
    def emitir_barulho(self):
        print(f'{self.nome} está dizendo POPO')