from rich import inspect, print
from rich.panel import Panel


class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(Panel(f'{self.nome:^5} \n {'-'*20} \n {self.preco:^5}', title = 'Produto'),)

p1 = Produto('Iphone 17', 10_000)

p1.etiqueta()        

