""" Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando cada dado num dicionário e todos os dicionários numa lista. 
No final mostre: 
a)Quantas pessoas foram registadas; 
b)Qual a média de idades do grupo; 
c)Quantas mulheres foram registadas; 
d)Quantos homens com idade acima da média foram registados. """

pessoas = dict ()
lista = list ()

qnt_mulheres = 0
qnt_pessoas = 0
qnt_homens = 0
homens = 0 
soma_idades = 0

while True:

    print("\nCADASTRO PESSOAS\n")
    pessoas["nome"] = input("Digite o nome: ").upper().strip()
    pessoas["sexo"] = input("Digite o sexo (M/F): ").upper().strip()
    if pessoas["sexo"] ==  'F':
        qnt_mulheres += 1
    elif pessoas["sexo"] == 'M':
        qnt_homens += 1
    pessoas["idade"] = int(input("Digite a idade: "))
    
    lista.append(pessoas)
         
    qnt_pessoas += 1

    continuar = input("\nDeseja continuar? [S/N]").upper().strip()

    if continuar != "S":
        break

for x in range(0, len(lista)):
     soma_idades += lista[x]["idade"]
media = soma_idades / qnt_pessoas

print(f"Quantidade Pessoas: {qnt_pessoas}")
print(f"Número de mulheres: {qnt_mulheres}")
print(f"Número de Homens: {qnt_homens}")
print(f"A média de idades é {media} anos.")
