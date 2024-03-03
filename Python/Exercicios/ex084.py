"""Desenvolva uma classe Temperatura que armazene a temperatura em graus Celsius como um atributo privado. Implemente um getter e um setter usando property para permitir que a temperatura seja ajustada e lida em Celsius, e adicione métodos para converter a temperatura para Fahrenheit e Kelvin."""

class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            print("\033[0;31mTemperatura negativa não permitida!\033[m")
            self.__celsius = None
        else:
            self.__celsius = valor

    def converter_para_fahrenheit(self):
        self.fahrenheit = (self.__celsius * 9/5) + 32
        return self.fahrenheit

    def converter_para_kelvin(self):
        self.kelvin = self.__celsius + 273.15
        return self.kelvin
    
# Teste da classe Temperatura

celsius_temp = Temperatura(25)
print(f"Temperatura em Celsius: {celsius_temp.celsius}")

# Convertendo e exibindo a temperatura em Fahrenheit
fahrenheit_temp = celsius_temp.converter_para_fahrenheit()
print(f"Temperatura em Fahrenheit: {fahrenheit_temp}")

# Convertendo e exibindo a temperatura em Kelvin
kelvin_temp = celsius_temp.converter_para_kelvin()
print(f"Temperatura em Kelvin: {kelvin_temp}")