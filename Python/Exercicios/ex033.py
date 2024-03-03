""" Crie um programa que leia vários números inteiros e que termine apenas quando o utilizador digitar a opção para parar. No final mostre quantos números o utilizador inseriu e qual a soma entre eles. """

cont, soma = 0, 0
num = int(input("Digite um número [0 para parar]: "))

while num != 0:
    soma += num
    cont += 1
    num = int(input("Digite um número [0 para parar]: "))
print(f"Digitou {cont} números e a soma entre eles foi {soma}")