""" Escreva um programa que leia um número N inteiro qualquer e mostre os N primeiros elementos de uma sequência de Fibonacci. 

Na matemática, a sucessão de Fibonacci, é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores. """

# Com a Biblioteca Fibonacci 

""" from fibonacci import fibonacci 

num = int(input(" Digite um numero que quer saber a sequencia Fibonacci:\n---> "))

fib = fibonacci(num)
print("A sequência de Fibonacci do número é:\n",fib) """

# Sem a biblioteca Fibonacci utilizando for 
"""num = int(input(" Digite um numero que quer saber a sequencia Fibonacci:\n---> "))
f1 = 0
f2 = 1
contador = 0

print(f1, end=' ') #Antes do loop vai imprimir o f1 que é 0 - primeiro numero fixo no Fibonacci
print(f2, end=' ') #Antes do loop vai imprimir o f2 que é 1 - segundo numero fixo no Fibonacci
for i in range(2, num): # 2 caracteres que vai fazer a sequencia
    f3 = f1 + f2
    print(f3, end=' ')
    f1 = f2 # F1 vai receber o F2
    f2 = f3 # F2 vai receber o F3"""


# Utilizando While - correção Ricardo 

print("-" * 22)
print("Sequência de Fibonacci")
print("-" * 22)

n = int(input("Quantos elementos que mostrar?\n---> "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Por favor, insira um número positivo.")
elif n == 1:
    print("Sequência de Fibonacci até", n, ":")
    print(a)
else:
    print("Sequência de Fibonacci:")
    while count < n:
        print(a, end=' ~ ')
        nth = a + b
        # atualizando os valores
        a = b
        b = nth
        count += 1
print("FIM")
