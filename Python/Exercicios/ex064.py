""" Crie um programa que tenha uma função que converta a temperatura de Celsius para Fahrenheit. """

""" °F = (°C x 1,8) + 32 """

def conversor(celsius):
    fahrenheit =  (celsius * 1.8) + 32
    return fahrenheit

celsius = float(input("Qual a temperatura em celsius? "))

print(f"\n{celsius}ºC equivale a {conversor(celsius)}°F")
    
    