""" Crie um programa que leia um número inteiro e peça ao utilizador para escolher a base de conversão
 1 - Binario
 2 - Octal
 3 - Hexadecimal """

seu_numero = int(input('Digite um número inteiro: '))

conversao = int(input("Escolha a conversão:\n1 - Binario\n2 - Octal\n3 - Hexadecimal\nDigite a operação desejada: "))
binario = bin(seu_numero)[2:]
octal = oct(seu_numero)[2:]
hexadecimal = hex(seu_numero)[2:]

if conversao == 1:
    print(f"A sua conversão em Binário é de {binario}")
elif conversao == 2:
    print(f"A sua conversão em Octal é de {octal}")
elif conversao == 3:
    print(f"A sua conversão em Hexadecimal é de {hexadecimal}")
else:
    print("Erro")
