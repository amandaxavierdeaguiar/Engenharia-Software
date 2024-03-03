""" Crie um programa que tenha uma função que receba vários parâmetros como valores inteiros. O programa deve analisar todos os valores e dizer qual deles é o maior. """

"""o asterisco antes de valores é usado para "desempacotar" a lista e passar seus elementos como argumentos individuais para a função maior_valor."""
def maior_valor(*valores):
    return max(valores)

valores = []
while True:
    valor = int(input("Digite um valor inteiro (-1 para parar): "))
    if valor == -1:
        break
    valores.append(valor)

print(f"O maior valor entre os informados é {maior_valor(*valores)}.")