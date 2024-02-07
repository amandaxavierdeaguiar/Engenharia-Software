""" Crie um programa onde o utilizador possa inserir uma equação matemática que use parênteses. O programa deverá analisar a equação e dizer se a equação tem os parênteses corretos ou se está errado.
ERRADO: ((a+b)-c(c/d)
CERTO:((a+b)-c(c/d)) """

lista = list()

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
                print("Expressão INCORRETA!")

