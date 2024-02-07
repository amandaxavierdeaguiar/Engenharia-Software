class Personagem:
    def __init__(self, nome):
        self._nome = nome.strip()
        self._vida = 100
        self._experiencia = 0
        self._nivel = 1

    def __str__ (self):
        return f'-- PERSONAGEM --\nNOME: {self._nome}\nPONTOS VITAIS: {self._vida}\nNÍVEL:{self._nivel}'

    @property
    def nome(self):
        return f'Personagem: {self._nome}'
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.strip().capitalize()

    @property
    def vida(self):
        return f'PONTOS VITAIS: {self._vida}'

    @property
    def experiencia(self):
        return f'XP: {self._experiencia}'
    
    @property
    def nivel(self):
        return f'NIVEL: {self._nivel}'

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self._poder = None
        self.varinha = "Pau"


    def __str__ (self):
        return f'-- MAGO --\nNOME: {self._nome}\nPONTOS VITAIS: {self._vida}\nXP:{self._experiencia}\nNÍVEL:{self._nivel}\nPODER: {self.poder}\nVARINHA {self.varinha}'

    
    
    @property
    def poder(self):
        return 'Nenhum poder disponivel' if self._poder == None else f'PODER: {self._poder}'
    
    @poder.setter
    def poder(self, novo_poder):
        self._poder = novo_poder




"""novo_mago = Mago('Amanda')


print(novo_mago)"""



"""novo_personagem = Personagem("Amanda")
print(novo_personagem.nome)
novo_personagem.nome = "Bianca"
print(novo_personagem.nome)
print(novo_personagem.nivel)
print(novo_personagem.vida)
print(novo_personagem.experiencia)
"""