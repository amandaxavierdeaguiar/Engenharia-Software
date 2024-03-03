""" Crie um programa que guarde o aproveitamento de um jogador de futebol. O programa deverá ler o nome, quantos jogos jogou e a quantidade de golos por jogo e guardar tudo num dicionário. No dicionário, deve calcular a média de golos por jogo. """

jogador = dict ()
lista = list ()

while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['qnt_jogos'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    jogador['gols'] = int(input(f'Quantos gols o {jogador["nome"]} fez? '))
    jogador["media"] = jogador["gols"] / jogador["qnt_jogos"] 

    lista.append(jogador.copy())
    print(jogador)

    continuar = str(input('Deseja continuar?[S/N]')).lower()

    if continuar != 's':
        print("\n--- Aproveitamento jogador ---\n")
        for e in lista:
            for k in e.items():
                print(k)
        break



