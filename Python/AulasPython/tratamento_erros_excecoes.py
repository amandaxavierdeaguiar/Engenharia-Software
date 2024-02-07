def divisao(a,b):
    div = a / b
    return div

try: 
    num1 = int(input("Digite o primeiro numero\n---> "))
    num2 = int(input("Digite o segundo numero\n---> "))
    print (divisao(num1, num2))
except Exception as erro:
    print(f"ERRO! CAUSA ---------> {erro.__doc__}")
"""except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("O valor informado não é numérico.")
except KeyboardInterrupt:
    print("O programa foi fechado inesperadamente!")
else: 
    print("Divisão é possível!")
finally: 
    print("O processamento foi finalizado.")"""

"""except Exception as erro:
    print(f"ERRO! CAUSA ---------> {erro.__class__}")"""