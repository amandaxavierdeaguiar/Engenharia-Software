""" Crie um programa com uma função que vai funcionar como a função input(), no entanto vai fazer a validação para aceitar apenas um valor numérico. """

def validacao(num):
    if num // 1 == num:
        return f"O {num:.0f} é um valor INTEIRO"
    else:
        return f"O {num} não é um número INTEIRO"

numero = float(input("Digite: "))
print(validacao(numero))