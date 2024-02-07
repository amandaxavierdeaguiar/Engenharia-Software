""" 
Crie uma classe chamada Livro e que tenha os atributos:
titulo, ano, autor e disponibilidade.
Utilize getters e setters para manipular as propriedades.
"""

class Livro:
    def __init__(self):
        print('A começar a criar titulo')
        self.__titulo = ""
        self.__ano = 2
        self.__autor = ""
        self.__disponibilidade = False

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def ano(self, autor):
        self.__autor = autor

    @property
    def disponibilidade(self):
        if disponibilidade:
            return f'O livro esta disponivel.'
        else:
            return f'O livro não se encontra disponível'
    
    @disponibilidade.setter
    def disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade
    
print("--Biblioteca")
titulo = input("Titulo: ")
ano = int(input("Ano: "))
autor = input("Autor: ")
disponibilidade = input("DISPONIBILIDADE").strip().lower()
if disponibilidade == 's':
    disponibilidade = True
else:
    disponibilidade = False


livro = Livro()
livro.titulo = titulo
livro.ano = ano
livro.autor = autor
livro.disponibilidade = disponibilidade

print("\n--Exibindo informações do livro:")
print(f"Título: {livro.titulo}")
print(f"Ano: {livro.ano}")
print(f"Autor: {livro.autor}")
