from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print('--- Iniciando o Preparo! ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- Bebida finalizada! ---')

    def ferver_agua(self):
        print('Fervendo a água para a bebida')


    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def misturar(self):
        print('Misturando o café')

    def servir(self):
        print('Café servido')

class Cha(BebidaQuente):

    def misturar(self):
        print('Misturando o chá')

    def servir(self):
        print('Chá servido')

class Leite(BebidaQuente):

    def misturar(self):
        print('Misturando o leite')

    def servir(self):
        print('Leite servido')
