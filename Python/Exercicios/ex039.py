""" Crie um programa que com um tuplas com os 20 primeiros classificados do Campeonato Espanhol de Futebol. Depois mostre: 
a)Os primeiros 5 classificados. 
b)Os últimos 4 classificados. 
c)Uma lista com as equipas por ordem alfabética. 
d)A posição da equipa Las Palmas. """

campeoes = ("Real Madrid - 1°", "Girona - 2°", "Atlético de Madri - 3°", "Barcelona - 4°", "Athletic Bilbao - 5°", "Real Sociedad - 6°", "Betis - 7°", "Valencia - 8°", "Getafe - 9°", "Las Palmas - 10°", "Rayo Vallecano - 11°", "Osasuna - 12°", "Villarreal - 13°", "Mallorca - 14°", "Alavés - 15°", "Sevilla - 16°", "Celta - 17°", "Cádiz - 18°", "Granada-ESP - 19°", "Almería - 20°")

print("\nOs primeiros 5 colocados:")
print(campeoes[:5])
print("\nOs ultimos 4 colocados:")
print(campeoes[-4:])
ordem = sorted(campeoes)
print("\nEquipes em ordem alfabética:")
print(ordem)
posicao = len("Las Palmas")
print("\nPosição da equipa Las Palmas:", posicao)
