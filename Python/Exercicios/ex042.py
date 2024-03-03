""" Crie um programa que tenha uma tupla com nome de jogos e seus respectivos preços em sequencia. No final mostre uma listagem de preços organizados em tabela. """

# FORMA QUE EU FIZ

"""jogo = ("Crash", "Super Mario", "Minecraft", "Fifa")
preco = ("29,99", "54,00", "38,90", "49,99" )
seta = ("." * 23)
txt = "JOGOS PARA NINTENDO SWITH"

titulo = txt.center(50)

print("\n")
print(titulo)
print("-" * 45)
print(f"\n{jogo[0]:<10} {seta:^10} {preco[0]:>10}\n")
print(f"\n{jogo[1]:<10} {seta:^10} {preco[1]:>9}\n")
print(f"\n{jogo[2]:<10} {seta:^10} {preco[2]:>10}\n")
print(f"\n{jogo[3]:<10} {seta:^10} {preco[3]:>10}\n")
print("-" * 45)
"""

#Abaixo, resolução Ricardo

jogos = ("Crash ", 29.99, 
        "Super Mario ", 54.00,
        "Minecraft ", 38.90, 
        "Fifa ", 49.99)

print("-" * 55)
print(f'{"LISTA DE JOGOS":^55}')
print("-" * 55)

for pos in range(0, len(jogos)):
    if pos % 2 == 0:
        print(f"{jogos[pos]:-<45}", end=" ")
    else:
        print(f"{jogos[pos]:>7.2f}€")
print("_" * 55)