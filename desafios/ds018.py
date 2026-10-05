from rich import print

class Churrasco():

    def __init__(self, qtd):
        self.qtd = qtd

    def qtd_carne(self, g_pessoa):
        qtd_carne = self.qtd * g_pessoa
        print(f'Quantidade de carne a ser comprada: {qtd_carne} kg')
        return qtd_carne

    def custo_total(self, preco, qtd_carne):
        c_total = preco * qtd_carne
        print(f'Custo total da compra da carne R$ {c_total:,.2f}')
        return c_total

c1 = Churrasco(10)
qtd_carne = c1.qtd_carne(0.4)
c_total = c1.custo_total(80, qtd_carne)

   
