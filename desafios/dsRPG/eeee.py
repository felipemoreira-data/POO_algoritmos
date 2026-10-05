import random
from rich import print

dicionatrio_golpes = {
    'Chute': 23,
    'Soco': 45,
    'Cotovelada': 34
}
lista =[i for i in dicionatrio_golpes.keys()]
golpe = random.choice(lista)
print(f'O usuário X deferiu um {golpe} causando {dicionatrio_golpes[golpe]} de [bold red]dano[/bold red] no usuário Y')