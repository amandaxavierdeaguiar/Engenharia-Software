""" Cria um programa que crie palpites para o Euromilhões. O programa deve perguntar quantas chaves serão geradas e deve sortear aleatoriamente 5 números de 1 a 50 [sem repetir] e 2 estrelas de 1 a 12 [sem repetir]. Cada sorteio deve ser guardado numa lista composta. """

from random import randint

print(f"{'EUROMILHÕES':^40}")


palpites = int(input("Quantos palpites deseja que eu crie?\n---> "))


for a in range(0, palpites):
    chave = [[], []]
    for i in range(0, 5):
        while True:
            num = randint(1, 50)
            if num not in chave[0]:
                chave[0].append(num)
                break

    for i in range(0, 2):
        while True:
            num = randint(1, 12)
            if num not in chave[1]:
                chave[1].append(num)
                break

    while True:
        # mostrar números
        print(f"Chave {a + 1:0>2}:", end=" | ")
        for numero in chave[0]:
            print(f"{numero:0>2}", end=" | ")
        print("", end=" | ")
        for estrela in chave[1]:
            print(f"*{estrela:0>2}", end=" | ")
        print("")
        break
print("Chaves geradas com sucesso! Boa sorte e volte sempre!")