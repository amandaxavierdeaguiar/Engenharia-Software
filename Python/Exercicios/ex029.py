""" Crie um jogo de adivinha que o computador deve pensar um número de 0 a 10 e o utilizador deve adivinhar o número escolhido.
O jogador deve tentar até acartar quantas vezes for necessário """
import random

jogo_pc = random.randint(0, 10) # o computador vai pensar num número aleatório

# print("Teste", jogo_pc)

tentativas = 0

input("Tente adivinhar um número de 0 a 10 escolhido pelo computador.\nAperte no ENTER para continuar...")

while True:
    adivinhe = int(input("\nTente Adivinhar o número escolhido\n--->"))

    if adivinhe > jogo_pc:
        print("\nO Número é menor,tente Novamente!")
        tentativas += 1
    elif adivinhe < jogo_pc:
        print("\nO Número é maior,tente Novamente!")
        tentativas += 1
    else:
        print("Parabéns, você ganhou!!!\n")
        break
print("Obrigado pela sua visita.\nVolte sempre!")
        
