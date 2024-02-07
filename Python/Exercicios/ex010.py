"""Crie um programa que lê um numero de 0 a 9999 e mostre cada um dos dígitos separados
Ex: 1992 
unidade: 2, dezena: 9, centena: 9 , milhar:1"""

numero = int(input("Digite um número inteiro de  de 0 a 9999: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
