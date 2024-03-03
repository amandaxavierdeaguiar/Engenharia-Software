""" Crie um programa que tenha uma função chamada area() que receba as dimensões de um terreno e mostre a área do terreno. """

def area(largura_terreno,  comprimento_terreno):
    
    area_terreno = largura_terreno * comprimento_terreno
    return f"A área do terreno é de: {area_terreno}"

largura_terreno = float(input("Qual a largura do terreno: "))
comprimento_terreno = float(input("Qual o comprimento do terreno: "))

print(area(largura_terreno, comprimento_terreno))


