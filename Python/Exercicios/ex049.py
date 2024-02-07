""" Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz com a formatação adequada. """

lista = [[0,0,0], [0,0,0], [0,0,0]]

for indice in range(0,3):
    for valor in range(0,3):
        lista[indice][valor] = int(input(f"Digite o numero[{indice}][{valor}]: "))

# print("\n",lista[0],"\n", lista[1],"\n", lista[2])

for indice in range(0,3):
    for valor in range(0,3):
        print(f"[ {lista[indice][valor]} ]", end= "")
    print()
