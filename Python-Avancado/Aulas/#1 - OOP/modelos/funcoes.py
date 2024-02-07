from modelos.classes import Personagem, Mago

def main():
    personagem = Personagem('Amanda')
    print(personagem)
    print('\n\n')
    novo_mago = Mago('Bianca')
    print(novo_mago.nome)