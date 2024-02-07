""" Crie um programa que leia 10 números introduzidos pelo utilizador e guardeos numa lista que separe os valores pares dos ímpares. No final exiba os valores pares e ímpares por ordem crescente. """

numero = [[], []]

for n in range(0,10):
    num = int(input("Digite o Número desejado: "))
    if num % 2 == 0:
        numero[0].append(num)
    else:
        numero[1].append(num)

print("Todos seus números introduzidos: ", numero)
ordem_par = sorted(numero[0])
print(f"A ordem dos números pares: ", ordem_par)
ordem_impar = sorted(numero[1])
print(f"A ordem dos números ímpares são: ", ordem_impar)

