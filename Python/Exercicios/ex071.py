""" Escreva um programa que peça ao utilizador dois numeros e divida o primeiro pelo segundo. Utilize o tratamento de exceções para lidar com casos em que o segundo número é zero e quando a entrada não é número válido. """

def divisao(a,b):
    div = a / b
    return div

try: 
    num1 = int(input("Digite o primeiro numero\n---> "))
    num2 = int(input("Digite o segundo numero\n---> "))
    print (divisao(num1, num2))
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Digite um número válido.")
finally: 
    print("O processamento foi finalizado.")
