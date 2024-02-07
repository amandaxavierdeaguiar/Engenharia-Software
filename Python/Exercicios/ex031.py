""" Desenvolva um programa que leia um número qualquer e que mostre o seu fatorial.

 O fatorial (!) de um número n, representado por n!, é a multiplicação de n por seus antecessores maiores ou iguais a 1. Essa operação é muito comum em análise combinatória. """

print("fatorial (!)")
num = int(input("Qual valor que quer saber o fatorial: \n ---> "))

#iniciar o fatorial - tem de iniciar em 1 porque multiplicar por zero dá zero e por um dá o mesmo nº
fat = 1 

while num > 0:
    print(f"{num}", end="") # end para alterar de ir para outra linha.
    print(" x " if num > 1 else " = ", end="")
    fat *= num # *= para executar a operação aritmética correspondente e, em seguida, atribuir o resultado de volta à mesma variável.
    num -= 1
print(f"{fat}")


# Pode ser feito através da biblioteca: 
""" import math  #biblioteca para operações matemáticas

num = int(input("Qual valor que quer saber o fatorial?\n---> "))

fat = math.factorial (num)

print(fat)"""


