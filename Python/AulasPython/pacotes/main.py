import header
import matematica
# Pode ser: import matematica import calculadora

 
header("Calculadora Mágica")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
sinal = input("Qual operação deseja fazer [+ - x /]").strip().lower()

print(f"{num1} {sinal} {num2} = {matematica.calculadora(num1, num2, sinal)}")
#Se por no import matematica import calculadora tem que tirar o matematica. e sim so por matematica.calculadora(num1, num2, sinal)



