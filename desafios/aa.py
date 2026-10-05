dicionario = {
    'a': [1,2,3],
    'b': [1,2,3],
    'c': [4,5,6],
    'd': [7,6,5]
}

lista = [[key, values] for key, values in dicionario.items()]
print(lista[0][1][1])