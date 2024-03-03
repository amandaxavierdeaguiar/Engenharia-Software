""" Desenvolva um programa que permita ao utilizador calcular o seu Índice de Massa Corporal (IMC). O programa deve solicitar ao utilizador a sua altura e o seu peso. De seguida, utilizando uma função, deve calcular o IMC e o programa deve exibir uma mensagem com base no valor do IMC calculado. 
●IMC abaixo de 18,5: Abaixo do peso 
●IMC entre 18,5 e 24,9: Peso normal 
●IMC entre 25,0 e 29,9: Sobrepeso 
●IMC entre 30,0 e 34,9: Obesidade grau 1 
●IMC entre 35,0 e 39,9: Obesidade grau 2 
●IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida) """
""" peso (kg) ÷ (altura x altura) (m). """

def imc (peso, altura):
    indice_corporal = peso / (altura * altura)
    
    if indice_corporal  < 18.5:
        print("Abaixo do peso")
    elif indice_corporal <= 24.9:
        print("Peso Normal")
    elif indice_corporal <= 29.9:
        print("Sobrepeso")
    elif indice_corporal <= 34.9:
        print("Obesidade grau I")
    elif indice_corporal <= 39.9:
        print("Obesidade grau II")
    elif indice_corporal >= 40.0:
        print("Obesidade grau III - Mórbida")
    else:
        print("Valores  inválidos!")
    
    return indice_corporal

peso = float(input("Qual seu peso (kg)? "))
altura = float(input("Qual sua altura (m)? "))

print(imc(peso, altura))



