""" Ex 21 - Contagem regressiva - Faça um programa que simule contagem regressiva para passagem de ano de 10 até 0, com 1 segundo de pauda entre eles """

import time 
""" import playsound # biblioteca para por som """

segundos = 0

print('2024 está chegando ...\n')

for contagem in range(10, -1, -1):

    segundos - 1
    time.sleep(1)
    print(contagem) 

print('2024 está chegando ...\n')

# Outra opção...

""" for contagem in range(0,10):

    print(10 - contagem)
    time.sleep(1) """

print("\nFeliz Ano Novo")