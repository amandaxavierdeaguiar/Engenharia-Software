""" Adicione um método à classe desenvolvida no exercício anterior Livro que imprime uma descrição do livro no formato: “O livro com o titulo X foi escrito pelo autor Y". """

"""class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
livro1 = Livro("Cem dias entre céu e mar", "Amyr Klink")
print(f"O livro com o titulo {livro1.titulo} foi escrito pelo autor {livro1.autor}")

livro2 = Livro("O Alquimista", "Paulo Coelho")
print(f"O livro com o titulo {livro2.titulo} foi escrito pelo autor {livro2.autor}")

livro3 = Livro("As Esganadas", "Jô Soares")
print(f"O livro com o titulo {livro2.titulo} foi escrito pelo autor {livro1.autor}")"""

class Livrinho:
    def __init__(self, tit, aut):
        self.tit = tit 
        self.aut = aut
    
    def imprimir(self):
        print(f"O livro com o título {self.tit} foi escrito pelo autor {self.aut}")

l1 = Livrinho("Cem dias entre céu e mar", "Amyr Klink")
l1.imprimir()

l2 = Livrinho("O Alquimista", "Paulo Coelho")
l2.imprimir()

l3 = Livrinho("As Esganadas", "Jô Soares")
l3.imprimir()


    
