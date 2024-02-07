"""Crie um programa que leia o primeiro e o ultimo nome da pessoa e exiba as mensagens:
1 - Ola {nome}, o seu registro esta completo
2 - O seu email é {nome}@empresa.pt"""

nome_usuario = input("Digite seu nome: ").title().strip()
primeiro_nome = nome_usuario.split()[0]
ultimo_nome = nome_usuario.rsplit()[-1]

print(f"Olá {primeiro_nome} {ultimo_nome}, o seu registro esta completo")
print(f"O seu email é {primeiro_nome.lower()}{ultimo_nome.lower()}@empresa.pt")
