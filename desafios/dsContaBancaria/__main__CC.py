from classContaBancaria import *
from rich import inspect

def main():
    c1 = ContaBancaria(id = 1212, nome = 'Felipe', saldo = 4_500)
    # c1.sacar(saque = 1_200)
    # c1.nome = 'renan'
    # print(c1)
    inspect(c1, private = True)



if __name__ == '__main__':
    main()