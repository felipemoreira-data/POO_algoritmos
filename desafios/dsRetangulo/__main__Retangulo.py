from classRetangulo import Retangulo
from rich import inspect

def main():
    r1 = Retangulo()
    try:
        r1.base = 3
        r1.altura = 6
        r1.medidas = (9,-2)
    except Exception as e:
        print(f'Erro --> {e}')

    finally:
        print(r1.medidas)    


if __name__ == '__main__':
    main()