from classRpg import Personagem, Mago, Guerreiro


def main():
    p1 = Mago(nome = 'Melvin', vida = 100)
    p2 = Guerreiro(nome = 'Kratos', vida = 100)
    p1.atacar(p2)
    p2.curar()





if __name__ == '__main__':
    main()
    