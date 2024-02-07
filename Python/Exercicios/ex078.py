class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        self.__pi = 3.14159

    def get_raio(self):
        return f"O raio do circulo é {self.__raio}"
    
    def set_raio(self, raio):
        return f"O valor do raio foi modificado para {raio}"
        self.__raio = raio

    def calcular_area(self):
        return f"A área do círculo é: {self.__pi * self.__raio ** 2}"
    
    def calcular_perimetro(self):
        return f'O perimetro do círculo é {self.raio}'