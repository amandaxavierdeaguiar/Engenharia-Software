""" Crie um programa que tenha uma função que receba um número inteiro e mostre a tabuada desse número."""

def tabuada(numero):
    for i in range(1, 11):
        tabuada_2 = f"{numero} x {i} = {numero * i}"
        print(tabuada_2) 

while True:
    numero = int(input("Digite um número para ver a sua tabuada (0 ou negativo para sair): "))
    
    print(f"\nTabuada do número {numero}:\n")
    print(tabuada(numero))
    
    if  numero <= 0:
        break
    

