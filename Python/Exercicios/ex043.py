""" Crie um programa que leia 5 numeros e guarde-os numa lista. No final mostre o maior e o menor valor e a respectiva posição na lista. """

lista = list()

for cont in range(0,5):
    num = int(input("Digite um número: "))
    lista.append(num)
    print(f"O numero {num} foi adicionado com sucesso")

print("\n")
print("Os valores da sua lista são:")


for valor in lista:
    print(valor, end= " ")

menor = min(lista)
print(f"\n\nO menor número da lista foi: {menor}")
maior = max(lista)
print(f"\nO maior número da lista foi: {maior}")