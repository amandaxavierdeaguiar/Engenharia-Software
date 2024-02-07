""" Ex 20 - Crie um jogo de pedra, papel e tesoura """
import random
import time

print("\n")
print("/" * 28)
print("Jogo Pedra, Papel & Tesoura")
print("/" * 28)
time.sleep(1)
print("\nPrimeiro, fique atento as regras do Jogo:\nPedra ganha da tesoura (quebrando-a).\nTesoura ganha do papel (cortando-o).\nPapel ganha da pedra (embrulhando-a).\nSeu adversário é o computador.\n")
print("Boa sorte!\n")

jogo_pc = random.randint(1, 3)

# print(jogo_pc) - Apenas para teste, ver a opcao do random

time.sleep(2)
jogador = int(input("Escolha a sua opção:\n[ 1 ] Pedra\n[ 2 ] papel\n[ 3 ] tesoura?\nDigite: "))

print(jogador)


if jogo_pc == jogador:
    print("Empate.\nVocês tiveram a mesma ideia!")
elif jogo_pc == 1 and jogador == 3:
    print("O computador ganhou!\nO computador escolheu Pedra e você escolheu Tesoura.\nSua tesoura quebrou")
elif jogador == 1 and jogo_pc == 3:
    print("Você ganhou!!!\nO computador escolheu Tesoura e você escolheu Pedra.\nA tesoura do seu adversário está partida!")
elif jogo_pc == 3 and jogador == 2:
    print("O computador ganhou!\nO computador escolheu Tesoura e você escolheu Papel.\nSeu papel foi cortado... ")
elif jogador == 3 and jogo_pc == 2:
    print(f"Você ganhou!!!\nO computador escolheu Papel e você escolheu Tesoura.\nO papel do seu adversário foi cortado em diversos pedacinhos... ")
elif jogo_pc == 2 and jogador == 1:
    print(f"O computador ganhou!\nO computador escolheu Papel e você escolheu Pedra.\nEle embrulhou sua pedra...")
elif jogador == 2 and jogo_pc == 1:
    print(f"Você ganhou!!!\nO computador escolheu Pedra e você escolheu Papel.\nVocê embrulhou muito bem a pedra do seu adversário!")
else:
    print("Opção inválida!")
