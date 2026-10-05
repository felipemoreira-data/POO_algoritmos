from classCredencial import Credencial
from rich import inspect

def main():
    c1 = Credencial()
    c1.senha = 'minha_senha'

    valido = c1.validar('minha_senha')

    if valido:
        print('V')
    if not valido:
        print('F')    


if __name__ == '__main__':
    main()