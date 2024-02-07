""" Crie um programa que leia o nome completo de uma pessoa e mostre: 
1- O nome com todas as letras em maiúsculas.
2- O nome com todas as letras minúsculas
3- Quantidade de letras sem espaço.
4- Quantas letras tem o primeiro nome. """

nome = input("Digite seu nome: ").strip()

primeira_palavra = nome.split()[0]
num_caracteres = len(primeira_palavra)


print(f"O nome com todas as letras em minusculas {nome.lower()}")
print(f"O nome com todas as letras em maiusculas {nome.upper()}")
print("Quantidade de Letras {}".format(len(nome) - nome.count(" ")))
print(f"Quantidade de letras primeiro nome {num_caracteres}")

