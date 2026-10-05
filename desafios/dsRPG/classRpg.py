from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = {
            'Army Lock': 62,
            'Soco cruzado': 54,
            'Cotovelada': 41,
            'Chute': 41
        }

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            lista = [i for i in self.golpes.keys()]
            golpe = random.choice(lista)
            print(f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com um {golpe} de força {forca}')
            dano = self.golpes[golpe]
            alvo.receber_dano(dano)
            print(f'{self.vida} -> {alvo.vida} de vida')
        else:
            print(f'O ataque de {self.nome} em {alvo.nome} é impossível devido a ambos estarem mortos!')    

    def receber_dano(self, dano):
        self.vida -= dano
        print(f'{self.nome} recebeu dano de {dano}')

    @abstractmethod
    def curar(self):
        pass    


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)


    def curar(self):
        cura = 0
        while self.vida < 100:
            self.vida += 1
            cura += 1
        print(f'{self.nome} enrolou uma atadura de ferimentos e recuperou {cura} pontos de vida')

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        cura = 0
        while self.vida > 100:
            self.vida += 1
            cura += 1
        print(f'{self.nome} fez uma magia e recuperou {cura} pontos de vida')           