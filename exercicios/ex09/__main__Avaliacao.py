from classAvaliacao import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao(nome = 'Felipe', disciplina= 'Matemática')
    av1.set_nota(10)
    inspect(av1, private = True)


if __name__ == '__main__':
    main()
