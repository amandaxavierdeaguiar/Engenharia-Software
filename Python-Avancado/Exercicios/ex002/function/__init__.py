class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo.strip():
           raise ValueError("Título não pode ser uma string vazia")
        if not autor.strip():
           raise ValueError("Autor não pode ser uma string vazia")
        self._titulo = titulo.strip().capitalize()
        self._autor = autor.strip().capitalize()
        self._ano = ano

    def __str__ (self):
        return f'-- LIVRO --\nTÍTULO: {self._titulo}\nAUTOR: {self._autor}\nANO: {self._ano}'
  
    @property
    def titulo(self):
        return f'Titulo: {self._titulo}'
    
    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo.strip().capitalize()
        

    @property
    def autor(self):
        return f'Autor: {self._autor}'
    
    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor.strip().capitalize()
    
    @property
    def ano(self):
        return f'Ano: {self._ano}'
    
    @ano.setter
    def ano(self, ano):
        self._ano == ano