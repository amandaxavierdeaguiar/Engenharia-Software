""" Ex19 - Jogo de Adivinha: Crie um jogo de adivinha que o computador deve "pensar" 
num numero de 0 a 7 e o utilizador deve adivinhar o número escolhido. O programa deve 
apresentar se o utilizador venceu ou perdeu"""

import time
import random
""" A biblioteca Random pensa num número aleatório """

print("Jogo de Adivinha\n")
time.sleep(1) # Pausa para mostrar mensagem

numero_aleatorio = random.randint(0, 7)

print(numero_aleatorio)
# Imprimindo para teste! 

print("O computador pensou em um número entre 0 e 7....\n")

numero_escolhido = int(input("Escolha seu número da Sorte: "))
print("\nVejamos...\nSerá que acertou?\n")
time.sleep(3) # Pausa para mostrar mensagem

if numero_aleatorio == numero_escolhido:
    print(f"Você Acertou!\nEu escolhi o {numero_aleatorio} e você escolheu o {numero_escolhido}")
else:
    print(f"Tente Novamente!\nEu escolhi o {numero_aleatorio} e você escolheu o {numero_escolhido}")
