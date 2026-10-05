from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento


    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1_900 <= ano <= date.today().year:
            self._nascimento = ano

        else:
            raise ValueError(f'Ano {ano} é incorreto e não aceito!')

    @property
    def idade(self):
        idade = date.today().year - self.nascimento
        return idade

    @idade.setter
    def idade(self):
        raise PermissionError('Você não pode alterar a idade assim!')


class Aluno(Pessoa):

    cursos_oficiais = ['ADM', 'ENF', 'CC', 'ENG']
    def __init__(self, nome:str, nascimento:str, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso:str):
        if novo_curso.strip().upper() in Aluno.cursos_oficiais:
            self._curso = novo_curso.strip().upper()
        else:
            self._curso = None
            raise ValueError('Esse curso não existe dentre os cursos cadastrados!')

    def add_curso(self, novo_curso):
        curso = novo_curso.strip().upper()
        if 3 <= len(curso) <= 5:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f'Formato do curso {curso} é incorreto!')     


