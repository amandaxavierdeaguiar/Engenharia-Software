""" Desenvolva um programa em Python que permita o utilizador calcular seu índice de massa corporal IMC. O programa deve solicitar ao utilizador a sua altura e seu peso. Em seguida, deve calcular o IMC e o programa deve exibir a mensagem com base no valor calculado:

IMC ABAIXO DE 18.5 - 'Abaixo do Peso'
IMC Entre 18.5 e 24.9 - 'Peso Normal'
IMC Entre 25 e 29.9 - 'Sobrepeso'
IMC Entre 30 e 34.9 - 'Obesidade Grau I'
IMC Acima de 34.9 - 'Obesidade Grau II'
IMC acima do 40.0 - 'Obesidade Grau III - Obesidade Mórbida'


ATIVIDADE EM GRUPO - AMANDA XAVIER E JANDIRA PEDROSA
"""

import time

print("\n")
print("/" * 18)
print("Calculadora de IMC")
print("/" * 18)
time.sleep(1)

peso = float(input('\n\nDigite seu Peso(kg) - Exemplo: 54.7\n---> '))
altura = float(input('\nDigite sua Altura(m)- Exemplo: 1.70\n---> '))

imc = peso / (altura*altura)

""" Ver quantos Kg precisa Engordar ou Emagrecer"""
p1 = 18.5 * (altura * altura)
p2 = 24.9 * (altura * altura)
precisa_engordar = p1 - peso
precisa_emagrecer = peso - p2



time.sleep(1)

if imc < 18.5:
    print(f'\nSeu IMC é {imc:.1f}')
    print('Você está Abaixo do Peso!')
    time.sleep(1)
    print(f'\nVocê precisa engordar {precisa_engordar:.2f} kg')
elif imc <= 24.9:
    print(f"\nSeu IMC é {imc:.1f}")
    print('Você tem Peso Normal! Parabéns!')
elif imc <= 29.9:
    print(f'\nSeu IMC é {imc:.1f}')
    print('Você está com Sobrepeso! Cuidado!')
    time.sleep(1)
    print(f'\nVocê precisa emagrecer {precisa_emagrecer:.2f} kg')
elif imc <= 34.9:
    print(f'\nSeu IMC é {imc:.1f}')
    print('Você tem Obesidade de Grau I! CUIDADO!')
    print(f'\nVocê precisa emagrecer {precisa_emagrecer:.2f} kg')
elif imc <= 39.9:
    print(f'\nSeu IMC é {imc:.1f}')
    print('Você tem Obesidade de Grau II! CUIDADO!')
    time.sleep(1)
    print(f'\nVocê precisa emagrecer {precisa_emagrecer:.2f} kg')
elif imc >= 40:
    print(f'\nSeu IMC é {imc:.1f}')
    print('Você tem Obesidade de Grau III! Obesidade Mórbida!')
    time.sleep(1)
    print(f'\nVocê precisa emagrecer {precisa_emagrecer:.2f} kg')
else:
    print('Erro na entrada de dados!\nTente novamente...')
