from rich import inspect
from classesEx04 import Pessoa, Aluno, Professor, Funcionario


p1 = Aluno(nome ='felipe', idade = 19, curso = 'Dados', turma = 'Superior')
p1.fazer_aniversario()
inspect(p1, methods= True)

print('='*56)

p2 = Professor(nome = 'Ricardo', idade = 43, especialidade= 'Bio', nivel= 'Mestre')
p2.dar_aula()
