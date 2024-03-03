""" Crie o jogo Pedra, Papel, Tesoura com orientação para objetos. """

import random
import time

# Definição da classe Jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def escolher_jogada(self):
        return random.randint(1, 3)
    
    def escolher_jogada_jogador(self, jogador):
        jogada = int(input(f"{jogador}, digite \n[ 1 ] Pedra\n[ 2 ] Papel \n[ 3 ] Tesoura\n--->"))
        
        return jogada

# Definição da classe Jogo
class Jogo:
    def __init__(self):
        self.jogador = Jogador("Jogador")
        self.computador = Jogador("Computador")

    def iniciar(self):
        print("\n")
        print("/" * 28)
        print("Jogo Pedra, Papel & Tesoura")
        print("/" * 28)
        time.sleep(1)
        print("\nPrimeiro, fique atento as regras do Jogo:\nPedra ganha da tesoura (quebrando-a).\nTesoura ganha do papel (cortando-o).\nPapel ganha da pedra (embrulhando-a).\nSeu adversário é o computador.\n")
        print("Boa sorte!\n")

        # Gera a jogada do computador
        self.computador_jogada = self.computador.escolher_jogada()

        # Gera a jogada do jogador
        self.jogador_jogada = self.jogador.escolher_jogada_jogador(self.jogador.nome)

        self.resultado()

    def resultado(self):
        if self.jogador_jogada == self.computador_jogada:
            print("Empate.\nVocês tiveram a mesma ideia!")
        elif (self.computador_jogada == 1 and self.jogador_jogada == 3) or \
             (self.computador_jogada == 3 and self.jogador_jogada == 2) or \
             (self.computador_jogada == 2 and self.jogador_jogada == 1):
            print(f"O computador ganhou!\nO computador escolheu {self.obter_jogada(self.computador_jogada)} e você escolheu {self.obter_jogada(self.jogador_jogada)}.\n{self.obter_jogada(self.computador_jogada)} venceu {self.obter_jogada(self.jogador_jogada)}...")
        elif (self.jogador_jogada == 1 and self.computador_jogada == 3) or \
             (self.jogador_jogada == 3 and self.computador_jogada == 2) or \
             (self.jogador_jogada == 2 and self.computador_jogada == 1):
            print(f"Você ganhou!!!\nO computador escolheu {self.obter_jogada(self.computador_jogada)} e você escolheu {self.obter_jogada(self.jogador_jogada)}.\n{self.obter_jogada(self.jogador_jogada)} venceu {self.obter_jogada(self.computador_jogada)}!") 
        else: 
            print("Opção inválida!")

    def obter_jogada(self, jogada):
        if jogada == 1:
            return "Pedra"
        elif jogada == 2:
            return "Papel"
        elif jogada == 3:
            return "Tesoura"

if __name__ == "__main__":
    game = Jogo()
    game.iniciar()
