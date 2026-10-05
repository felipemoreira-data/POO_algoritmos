from classTermostato import Termostato
from rich import inspect

def main():
    t1 = Termostato()
    try:
        t1.temperatura = 34.2
        print(t1.temperatura)
    except Exception as e:
        print(f'Erro --> {e}')

    inspect(t1, private = True)


if __name__ == '__main__':
    main()    