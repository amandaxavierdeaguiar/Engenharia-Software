""" Crie uma classe chamada livro que tenha dois atributos: titulo e autor. 
Instancie três objetos dessa classe e e imprima os valores dos atributos. """

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
# Instanciando Objetos da Classe Livro
livro1 = Livro("Cem dias entre céu e mar", "Amyr Klink")
print(livro1.titulo, livro1.autor)

livro2 = Livro("O Alquimista", "Paulo Coelho")
print(livro2.titulo, livro2.autor)

livro3 = Livro("As Esganadas", "Jô Soares")
print(livro3.titulo, livro3.autor)

