""" Desenvolva o jogo par ou ímpar. O jogo só será interrompido quando o jogador perder e deverá exibir o total de vitórias consecutivas. """

from random import randint

print("-" * 17)
print("JOGO PAR OU ÍMPAR")
print("-" * 17)

v = 0

while True:
    jogador = int(input("\nDigite um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = input("Par ou ímpar? [P/I]\n-->").strip().upper()[0]
    print(f"O jogador digitou {jogador} e o computador {computador}. O total é {total}.")
    print("Deu par" if total % 2 == 0 else "Deu ímpar")
    if tipo == "P":
        if total % 2 == 0:
            print("PARABÉNS!!! Vences-te!")
            v += 1
        else:
            print("OHHHH! Perdes-te!")
            break
    if tipo == "I":
        if total % 2 == 1:
            print("PARABÉNS!!! Vences-te!")
            v += 1
        else:
            print("OHHHH! Perdes-te!")
            break
    print("Vamos voltar a jogar...")
print(f"GAME OVER! Ganhas-te {v} vezes.")