""" Ex18 - Crie um programa que leia dois números inteiros e compare-os da seguinte forma:  
O primeiro número é maior;
O segundo número é maior;
Os números são iguais """

numero1 = int(input("Digite o Primeiro número: "))
numero2 = int(input("Digite o Segundo número: "))

if numero1 > numero2:
    print("Seu primeiro número é maior que o Segundo número")
elif numero2 > numero1:
    print("Seu segundo número é maior que o primeiro número")
elif numero2 == numero1:
    print("Seus numeros são iguais.")
else:
    print("Tente novamente")
    