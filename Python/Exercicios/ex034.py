"""Crie um programa que leia várias notas introduzidas pelo utilizador. No final mostre quantas notas o utilizador inseriu, qual a média entre elas e qual a maior e a menor nota."""

resp = "S"
soma = quant = média = maior = menor = 0

while resp in "Ss":
    nota = float(input("Digite uma nota: "))
    soma += nota
    quant += 1
    if quant == 1:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    resp = input("Quer continuar? [S/N]: ").upper().strip()[0]
média = soma / quant
print(f"Digitou {quant} números e a média foi {média} valores.")
print(f"O maior valor foi {maior} e o menor foi {menor}")