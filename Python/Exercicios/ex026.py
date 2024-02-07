""" Ex 26 -  Faça um programa que leia 10 idades e mostre a maior e a menor idade """

# Inciar variaveis de controle
maior_idade = 0
menor_idade = 0

for pessoa in range(0, 10):
    idade = int(input(f"Digite a idade da {pessoa + 1} ? "))

    if pessoa == 0:
        # Guardar os dados
        maior_idade = idade
        menor_idade = idade

    else:
        if idade > maior_idade:
            maior = idade
        elif idade < menor_idade:
            menor = idade

print(f"A maior idade é {maior}")
print(f"A menor idade é {menor}")
