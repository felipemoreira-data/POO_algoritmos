from rich import inspect

class Gamer:
    def __init__(self, nome, apelido, favoritos = None):
        self.nome = nome
        self. apelido = apelido
        self.favoritos = list(favoritos) if favoritos else []

    def add_favoritos(self, jogo):
        self.favoritos += jogo

    def ficha(self):
        print(f'Nome real: {self.nome}')
        print(f'Jogos Favoritos: {[item for item in self.favoritos]}')


g1 = Gamer('Felipe', 'boca', ['mario', 'fifa'])
inspect(g1, methods= True)
# print(g1)
               