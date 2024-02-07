class Jogo:
    def __init__(self, titulo, consola, preco):
        self.titulo = titulo
        self.consola = consola
        self.preco = preco
        # Criando instâncias de jogos e acessando atributos

jogo = Jogo("God of War", "PlayStation 4", 39.90)

print(jogo.titulo)
print(jogo.consola)
print(jogo.preco)
