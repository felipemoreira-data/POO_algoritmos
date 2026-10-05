## Declaração da classe
class Gafanhoto:
    def __init__(self): ## Método construtor
        ## Atributos de instância
        self.nome = ''
        self.idade = 0

    ## Métodos de instância

    def aniversario(self):
        self.idade += 1

    def sobrenome(self):
        self.nome += ' moreira'    

    def mensagem(self):
        return f'O {self.nome} é o gafanhoto que tem {self.idade} anos de idade '    


## Declaração do Objeto
g1 = Gafanhoto()
g1.nome = 'felipe'
g1.idade = 19
g1.aniversario()
g1.sobrenome()
print(g1.mensagem())
