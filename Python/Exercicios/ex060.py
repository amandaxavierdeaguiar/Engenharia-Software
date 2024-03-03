""" Crie um programa que tenha uma função que receba 3 parâmetros: inicio, fim e passo. O programa deve realizar 3 contagens através da função. a)De 1 até 20, de 2 em 2 b)De 10 até 0, de 1 em 1 c)Contagem personalizada """

#Resolucao Ricardo

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("~" * 35)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=" ")
            cont += passo
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=" ")
            cont -= passo
        print("FIM!")


contador(1, 20, 2)
contador(10, 0, 1)
print()
print("~"*40)
print("Chegou a hora de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)
