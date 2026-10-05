from classesBq import BebidaQuente, Cafe, Leite, Cha
from rich import print


def main():
    print('[bold white]Seja Bem Vindo(a) a cafetaria![/bold white] :tea:')

    b1 = Cafe()
    b1.preparar()

    print('='*50)


    b3 = Cafe()
    b3.preparar()

    print('='*50)

    b2 = Leite()
    b2.preparar()


if __name__ == '__main__':
    main()