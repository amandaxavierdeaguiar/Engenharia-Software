""" Ex 25 -  Faça um programa que leia uma frase qualquer e diga se é um palídromo, desconsiderando os espaços """

frase =  input("Verifique se sua frase é um palíndromo: ").strip().upper()
palavras = frase.split()
juntas = "".join(palavras) # Retirando os espaços

inverter_texto = juntas[::-1]

print(inverter_texto)

if juntas == inverter_texto:
    print (f"Sua {frase} é um palíndromo!")
else:
    print ("Sua frase não é palindromo")
    