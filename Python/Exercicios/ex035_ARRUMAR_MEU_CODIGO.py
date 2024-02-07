""" Tabuada V2.0 – Faça um programa que mostre a tabuada de vários números inseridos pelo utilizador. O programa deverá ser interrompido quando o número inserido for negativo ou 0 """

#Arrumar o que tentei fazer, abaixo:
"""c, soma = 0, 0

tab = int(input("Digite um número para saber a tabuada:\n----> "))

while tab != 0:
    soma += tab
    c += 1
    print(tab, "x", (c + 1), "=", end= " ")
    tabuada = tab * (c + 1)
    print(tabuada)
    if c == 9:
        break
    elif tab == 0:
        break"""
    
while True:
    numero = int(input("Digite um número para ver a sua tabuada (0 ou negativo para sair): "))
    if numero <= 0:
        break

    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

print("Programa encerrado.")

