"""Crie um programa que sorteie a ordem de jogada num jogo ao “atirar um dado ao ar”. Cada jogador terá um número aleatório associado dentro de um dicionário. No final ordene o ranking para ver a ordem de jogada."""

from random import randint
from operator import itemgetter

jogo = {"Amanda": randint(1, 6),
        "Adilson": randint(1, 6),
        "Bianca": randint(1, 6),
        "Bia": randint(1, 6)
}

ranking = dict()

print("Valores sorteados:")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("=-" * 15)
print(f"{'Ranking:':^30}")
print("=-" * 15)
for i, v in enumerate(ranking):
    print(f"{i+1}.ª lugar ---> {v[0]} com {v[1]}.")