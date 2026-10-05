from abc import ABC, abstractmethod ## Abstract Base Classes


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'Matrícula de {self.nome} realizada com sucesso!')    

    def estudar(self):
        print(f'Aluno {self.nome} está estudando')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Aula do professor {self.nome} realizada com sucesso!')    

    def estudar(self):
        print(f'Professor {self.nome} está estudando para dar aula de {self.especialidade}')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'Ponto de {self.nome} batido!')

    def estudar(self):
        print(f'O funcionário está estudando para executar a função de {self.cargo}')