class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo.strip():
           raise ValueError("Título não pode ser uma string vazia")
        if not autor.strip():
           raise ValueError("Autor não pode ser uma string vazia")
        self.__titulo = titulo.strip().capitalize()
        self.__autor = autor.strip().capitalize()
        self.__ano = ano
  
    @property
    def titulo(self):
        return f'Titulo: {self.__titulo}'
    
    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo.strip().capitalize()
        

    @property
    def autor(self):
        return f'Autor: {self.__autor}'
    
    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor.strip().capitalize()
    
    @property
    def ano(self):
        return f'Ano: {self.__ano}'
    
    @ano.setter
    def ano(self, ano):
        self.__ano == ano