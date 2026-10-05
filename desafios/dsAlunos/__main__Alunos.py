from classAlunos import *
from rich import inspect


def main():
    a1 = Aluno(nome = 'felipe', nascimento= 2007, curso = 'ENF')
    a1.add_curso('dtsc')
    a1.curso = ' dtsc'
    print(a1.__dict__)
    print(Aluno.cursos_oficiais)
    
    

if __name__ == '__main__':
    main()