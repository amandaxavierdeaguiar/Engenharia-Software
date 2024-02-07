""" Desenvolva um programa que leia 3 valores e mostre o menu: 
[1] SOMAR 
[2] MULTIPLICAR 
[3] MAIOR 
[4] NOVOS NÚMEROS 
[5] SAIR DO PROGRAMA 
O programa deve realizar a operação solicitada em cada caso. """

controle = 0 

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))
num3 = int(input("Digite o primeiro número: "))

while controle != 5:
    
    operacao = int(input("\nQue operação quer realizar?\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA "))

    if operacao == 1:
        soma = num1 + num2 + num3
        print(f"O valor da soma dos números: {num1} + {num2} + {num3} = {soma}")
    elif operacao == 2:
        multiplicacao = num1 * num2 * num3
        print(f"O valor da multiplicação dos números: {num1} X {num2} X {num3} = {multiplicacao}")
    elif operacao == 3:
        if num1 > num2 and num1 > num3:
            print("O primeiro número é o maior")
        elif num2 > num1 and num2 > num3:
            print("O segundo número é o maior")
        elif num1 == num2 == num3:
            print("Os numeros são iguais")
        else:
            print("O terceiro numero inserido é o maior")
    elif operacao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o primeiro número: "))
        num3 = int(input("Digite o primeiro número: "))
        controle += 1  
