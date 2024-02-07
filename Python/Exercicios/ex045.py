""" Crie um programa onde o utilizador insira 5 números dentro de uma lista. Os valores devem ser registados já na posição correta [ordem crescente] e no final mostre a lista ordenada. Não utilizar o sort() """

lista = list()

for cont in range(0,5):
    num = int(input("Digite um número: "))
    if cont == 0:
        lista.append(num)
        print(f"O numero {num} foi adicionado com sucesso")
    elif num > lista[-1]: #Adicionado na ultima posicao
        lista.append(num)
        print(f"O numero {num} foi adicionado na ultima posição")
    else:
        contador = 0
        while contador < len(lista):
            if num <= lista[contador]:
                lista.insert(contador, num)
                print(f"O novo número adicionado na posição {contador + 1}")
                break
            contador += 1
    print(f"Os valores em ordem são: {lista}")

