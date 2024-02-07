""" Crie um programa que leia vários números e coloca-os numa lista. Crie duas listas adicionais que vão conter os números pares e impares da lista principal. No final mostre todas as listas. """

lista = list()

while True:
    num = int(input("Digite um número para adicionar a lista: ")) 
    lista.append(num)
    print("Valor adicionado com sucesso!")
    continuar = input("Deseja continuar?[S/N]").lower()

    while continuar == "n":
        print("Sua lista foi: ", lista)

        pares = list()
        impares = list()

        count = 0

        for par in lista:
            if par % 2 == 0:
                pares.append(par)
                count += 1
            else:
                impares.append(par)
                count += 1

        
        print(f"Os números pares são: {pares}")
        print(f"Os números ímpares são: {impares}")

        break
    