""" Crie um programa que leia 4 valores e guarde-os num tuple. No final exiba: 
a)Quantas vezes aparece o número 7. 
b)Em que posição foi digitado o número 5. 
c)Quais são os números pares. 
O programa deve informar quando não encontrar resposta. """
import random

valores = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(valores)

quantidade = valores.count(7)
print(f"O número 7 aparece: {quantidade} vezes")

if 5 in valores: 
    posicao = valores.index(5) 
    print(f"O número 5 está na {posicao} posição") 
else: print("O número 5 não foi digitado")

for num in valores:
    if num % 2 == 0:
        print(f"Os números pares são: {num}")

