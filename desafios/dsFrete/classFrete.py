from abc import ABC, abstractmethod
from rich import print

class Transporte(ABC):
    def __init__(self, distancia, frete = 0):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)

    def calc_frete(self, fator = 0.5):
        self.frete = fator * self.distancia
        return self.frete

class Caminhao(Transporte):
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)
    
    def calc_frete(self, fator = 1.20):
        if self.distancia > 50_000:
            self.frete = fator * self.distancia
            return self.frete
        else:
            return None

class Drone(Transporte):
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)
    
    def calc_frete(self, fator = 9.50):
        if self.distancia <= 10_000:
            self.frete = fator * self.distancia
            return self.frete
        else:
            return None
    