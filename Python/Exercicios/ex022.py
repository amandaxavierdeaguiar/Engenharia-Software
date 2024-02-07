""" Ex 22 - Faça um programa que mostre os números pares entre 1 e 100 """

i = 0
f = 100

for c in range(i, f):
    if c == 0:
        continue 
    elif c % 2 == 0:
        print(c) 

#  Continue - vai para a proxima condicao 
        