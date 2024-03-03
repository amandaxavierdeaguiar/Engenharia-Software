""" Crie um programa que tenha uma função que receba um texto como parâmetro e que mostre uma mensagem com tamanho adaptável. 
Ex: mostre(“Olá mundo.”) 
Saída:
-=-=-=-=-=-=-=-= 
    Olá mundo.
-=-=-=-=-=-=-=-= """

def mostra(msg):
    tam = len(msg)
    print("-=" * tam)
    print(f"     {msg}")
    print("-=" * tam)

mostra("Olá Mundo")

