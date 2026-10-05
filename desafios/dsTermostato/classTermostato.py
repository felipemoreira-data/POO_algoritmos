class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f'Temperatura inválida!')
        if 16 <= valor <= 30:
            self.__temperatura = valor
        if valor < 16:
            self.__temperatura = 16
        if valor > 30:
            self.__temperatura = 30

    @property
    def ftemperatura(self):
        return f'{self.temperatura} {chr(176)}C'


          