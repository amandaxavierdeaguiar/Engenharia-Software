""" Ex 24 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo """ 

# Numero primo - Apenas pode ser divido por ele mesmo ou pelo numero 1 

num = int(input('Digite um número:\n---> '))

tot = 0 # Variável de controle

for i in range(1, num + 1):
    if num % i == 0:
        tot += 1 # mesmo que tot = tot + 1

if tot == 2:
    print(f'O número {num} é PRIMO! Foi divisível {tot} vezes')
else:
    print(f'O número {num} NÃO É PRIMO! Foram divisíveis {tot} vezes')
    