from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        perimetro_n = self.qtd_lados * self.lado
        print(f'Perímetro do quadrado {perimetro_n:.2f}')

    def area(self):
        area_n = self.lado ** 2
        print(f'Área do quadrado {area_n:.2f}')

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(None)
        self.raio = raio

    def perimetro(self):
        perimetro_n = 2 * pi * self.raio
        print(f'Perímetro do círculo {perimetro_n:.2f}')

    def area(self):
        area_n = pi * (self.raio ** 2)
        print(f'Área do circulo {area_n:.2f}')               