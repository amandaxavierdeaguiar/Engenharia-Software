"""
Desenvolva um programa que simule uma calculadora interativa com diferentes funcionalidades. O programa deve exibir um menu com várias opções e permitir que o utilizador escolha uma das opções. O programa deve executar a funcionalidade escolhida e quando terminar deve voltar a apresentar o menu. Use o tratamento de exceções para lidar com entradas inválidas (como strings ou caracteres) e erros matemáticos (como divisão por zero). Todas as funções devem estar num módulo bem estruturado e documentado. 
Função-Calculadora [SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO] 
Função-Tabuada 
Função-Par ou Ímpar 
Função-Números primos 
Função-Factorial
"""
from calculadora import *
from tabuada import *
from par_impar import *
from primos import *
from fatorial import *

print('-' * 40)
print("Calculadora".center(40))
print('-' * 40)
print("Que operação deseja realizar?".center(40))
print()
try: 
    while True:
        op = int(input("\033[033m[ 1 ] Soma\n[ 2 ] Subtração\n[ 3 ] Multiplicação\n[ 4 ] Divisão\n[ 5 ] Tabuada\n[ 6 ] Par ou Impar\n[ 7 ] Números Primos\n[ 8 ] Fatorial\n[ 9 ] Sair\n\033[m"))
        if op == 1:
            num1 = int(input("Digite o primeiro numero\n---> "))
            num2 = int(input("Digite o segundo numero\n---> "))
            print (f"{num1} + {num2} = ", soma(num1, num2))
        elif op == 2:
            num1 = int(input("Digite o primeiro numero\n---> "))
            num2 = int(input("Digite o segundo numero\n---> "))
            print (f"{num1} - {num2} = ",subtracao(num1, num2))
        elif op == 3:
            num1 = int(input("Digite o primeiro numero\n---> "))
            num2 = int(input("Digite o segundo numero\n---> "))
            print (f"{num1} x {num2} = ",multiplicacao(num1, num2))
        elif op == 4:
            num1 = int(input("Digite o primeiro numero\n---> "))
            num2 = int(input("Digite o segundo numero\n---> "))
            print (f"{num1} / {num2} = ", divisao(num1, num2))
        elif op == 5:
            num = int(input("Digite o numero\n---> "))
            print(tabuada(num))
        elif op == 6:
            num1 = int(input("Digite o numero\n---> "))
            print(f"O número {num1} é: ", parEimpar(num1))
        elif op == 7:
            num = int(input("Digite o numero\n---> "))
            print(primos(num))
        elif op == 8:
            numero = int(input("Insira um número para ver o seu fatorial: "))
            opcao = input("Deseja ver o processo? [S/N]\n---> ").strip().lower()
            mostra = True if opcao == "s" else False
            resultado = fatorial(numero, mostra)
            print(resultado)
        elif op == 9:
            break       
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Digite um número válido.")
finally: 
    print("O processamento foi finalizado.")
