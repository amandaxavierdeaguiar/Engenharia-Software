# lista = [2,3,4,5]
"""nova_lista = lista[:] #[:] -> Cria uma copia da lista
nova_lista[0] = 7 


print(f"Esta é a lista princial: {lista}")
print(f"Esta é a nova lista {nova_lista}")"""

"""for i, v in enumerate(lista): # a primeira variavel é sempre o indice e a segunda é o valor que colocou
    print(i,v)"""

lista = list()

for cont in range(0,5):
    num = int(input("Digite um número: "))
    lista.append(num)
    print(f"O numero {num} foi adicionado com sucesso")

for valor in lista:
    print(valor, end= " ")


lista.pop(0) # Se por o indice, apaga qual colocou, se nao colocar o indice, apaga sempre o ultimo

for valor in lista:
    print("\n", valor, end = " ")
