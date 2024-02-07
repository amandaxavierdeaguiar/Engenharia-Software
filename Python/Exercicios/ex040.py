""" Crie um programa que gere 5 números aleatórios dentro de uma tupla. Depois mostra a listagem de números gerados, o menor e o maior da lista.
"""
import random

numeros = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))

print("Listagem de números gerados:", numeros)

menor = min(numeros)
maior = max(numeros)

print("Menor número:", menor)
print("Maior número:", maior)
