#Cria um programa que leia dois valores introduzidos e que apresente a sua SOMA, SUBTRACAO, MULTIPLICACAO E RESTO

print('Operacoes Matemáticas\n'.center(30))
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

print(f'O resultado da soma é: {soma}')
print(f'O resultado da subtracao é: {subtracao}')
print(f'O resultado da multiplicacao é: {multiplicacao}')
print(f'O resultado da divisao é: {divisao}')
print(f'O resultado da divisao é: {resto}')
