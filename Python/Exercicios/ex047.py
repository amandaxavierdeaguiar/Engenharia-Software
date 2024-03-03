""" Crie um programa onde o utilizador possa inserir uma equação matemática que use parênteses. O programa deverá analisar a equação e dizer se a equação tem os parênteses corretos ou se está errado.
ERRADO: ((a+b)-c(c/d)
CERTO:((a+b)-c(c/d)) """

#Tentei desenvolver abaixo
"""lista = list()

contador = 0

while True:
    expressao = input("Digite sua expressão matemática: ")
    lista.append(expressao)
    continuar = input("Deseja continuar?[S/N]").lower()

    print(lista["(":")"])

    while continuar == "n":
        for parenteses in lista:
            contador += 1

            if lista["(":")"]:
                print("Expressão CORRETA.")
            else:
                print("Expressão INCORRETA!")"""

#Resolucao Ricardo
lista = list()
equacao = input("Digite a sua equação:\n---> ")
quantidade_parentises = 0

for letra in equacao:
    lista.append(letra)

for letra in lista:
    if letra == "(" or letra == ")":
        quantidade_parentises += 1

if quantidade_parentises % 2 == 0:
    print("A sua equação funciona.")
else:
    print("A sua equação está errada!")