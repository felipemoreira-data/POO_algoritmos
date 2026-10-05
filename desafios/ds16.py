from rich import inspect

class Funcionario():
    ## Atributos de Classe
    empresa = 'Banco Do Brasil'

    def __init__(self, nome, setor, cargo):
        ## Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __repr__(self) -> str:
        return f'Prazer meu nome é {self.nome}, sou do setor {self.setor} e atuo no cargo de {self.cargo} na empresa {Funcionario.empresa}'

## Funcionario.empresa
## self.__class__.empresa
p1 = Funcionario('joao', 'logística', 'otimização operacional')

# inspect(p1)
inspect(Funcionario)