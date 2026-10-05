from classDiario import Diario
from rich import inspect


def main():
    d1 = Diario()

    try:
        d1.escrever('Não gosto do meu professor!')
    except Exception as e:
        print(f'erro --> {e}')

    try:
        d1.ler('Cl#2')
    except Exception as e:
        print(f'erro --> {e}')

    # try:
    #     d1.senha = ('Cl#2', '98X@2')
    # except Exception as e:
    #     print(f'Erro --> {e}')
    # finally:
    #     inspect(d1, private= True)                     

if __name__ == '__main__':
    main()