""" Melhore o exercício 49, exibindo no final. a)A soma de todos os valores pares. b)A soma dos valores da segunda coluna. c)O maior valor daterceira linha. """

lista = [[0,0,0], [0,0,0], [0,0,0]]

for indice in range(0,3):
    for valor in range(0,3):
        lista[indice][valor] = int(input(f"Digite o numero[{indice}][{valor}]: "))

# print("\n",lista[0],"\n", lista[1],"\n", lista[2])

for indice in range(0,3):
    for valor in range(0,3):
        print(f"[ {lista[indice][valor]} ]", end= "")
    print()

#soma valores pares:
"""for p in range(0, len(lista)):
    if lista[0][valor] % 2 == 0:
        soma = lista[0][valor] + lista[1][valor] + lista[2][valor]
        print(f"A soma dos números são {soma}")"""

for indice in range(0, len(lista)):
    for valor in range(0, len(lista)):
         if lista[0][valor] % 2 == 0:
            soma = lista[0][valor] + lista[1][valor] + lista[2][valor]
            