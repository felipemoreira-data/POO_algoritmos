from classAvaliacaoP import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao(nome = 'Felipe', disciplina= 'Matemática')
    av1.nota = 7.8
    inspect(av1, private = True)
    print(f'{av1.nome} tirou {av1.nota} na prova')

if __name__ == '__main__':
    main()
