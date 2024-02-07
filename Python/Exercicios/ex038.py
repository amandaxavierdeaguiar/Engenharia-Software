""" Crie um programa que leia um número de 0 a 20 introduzido pelo utilizador. Depois deverá mostrar por extenso o número introduzido. """

numero_extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatrorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezonove", "Vinte")

num = int(input("Digite um número: "))

print(f"Seu número '{num}' por extenso é: ",numero_extenso[num])
