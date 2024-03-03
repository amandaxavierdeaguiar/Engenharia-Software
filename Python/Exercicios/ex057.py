""" Melhore o exercício 55 para que permita a entrada de vários jogadores. Defina um sistema de visualização que permita ao utilizar procurar pelos resultados de um jogador específico. """

jogador = dict ()
lista = list ()

while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['qnt_jogos'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    jogador['gols'] = int(input(f'Quantos gols o {jogador["nome"]} fez? '))
    jogador["media"] = jogador["gols"] / jogador["qnt_jogos"] 

    lista.append(jogador.copy())
    print(jogador)

    continuar = input('Deseja continuar?[S/N]').lower()

    if continuar != 's':
        print("\n--- Aproveitamento jogador ---\n")
        for e in lista:
            for k, v in e.items():
                print(f"{k}: {v}")
        
        print("\nAgora, você pode procurar um jogador específico.\n")
        
        search_name = input("Digite o nome do jogador que deseja procurar: ").strip().upper()
        found = False
        for player in lista:
            if search_name == player['nome'].strip().upper():
                print("\nJogador encontrado:")
                for k, v in player.items():
                    print(f"{k}: {v}")
                found = True
                break
        if not found:
            print("Jogador não encontrado.")
        break
    
    
    
    