from rich.pretty import pprint
from rich import inspect
class Bird:

    def __init__(self, nome, comidas = None, voa = True, extinto = False):
        self.nome = nome
        self.comidas = list(comidas) if comidas else []
        self.voa = voa
        self.extinto = extinto


    def __repr__(self):
        return f'O pássaro {self.nome} come {self.comidas} {', voa' if self.voa == True else ' '} {'e está extinto.' if self.extinto == True else '.'}'


birds = {
    'pombo': Bird(nome = 'Pombo', comidas= ['minhoca', 'pao'], voa = True, extinto= False),
    'dodo': Bird(nome = 'Dodo', comidas = ['folha', 'fruta'], voa = False, extinto= True)
}

inspect(birds)