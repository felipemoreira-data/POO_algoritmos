import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from interface.interface import texto

## Declaração da classe
class Gafanhoto:
    ''' Essa classe cria um novo gafanhoto, que é uma pessoa que recebe atributos como
    nome, idade, sexo e estado civil
        Para criar uma nova pessoa, use 
        variavel = Gafanhoto(nome, idade...)
    '''
    def __init__(self, nome, idade, sexo = '', ec = ''): ## Método construtor
        ## Atributos de instância
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.ec = ec

    ## Métodos de instância

    def aniversario(self):
        self.idade += 1

    def sobrenome(self):
        self.nome += ' moreira'    

    def __str__(self): ## Método Dunder Method
        return f"O {self.nome} é o gafanhoto que tem {self.idade} anos de idade sexo {self.sexo}, com estado civil {self.ec}"    

    def __getstate__(self):
        return f'eu : {self.nome}, tempo_vida : {self.idade}'

## Declaração do Objeto
g1 = Gafanhoto('felipe', 19)
g1.aniversario()
g1.sobrenome()
print(g1)
print(g1.__dict__) ## Atributo / Dunder Attributte
print(g1.__getstate__()) ## Método / Dunder Method (Pode ser personalizável)
print(g1.__class__)
print(g1.__doc__)

#texto(g1.__doc__)
