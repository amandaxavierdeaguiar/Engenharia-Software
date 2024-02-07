""" Crie um jogo que faça 3 perguntas ao utilizado e que apenas aceite resposta V ou F. Caso esteja errado, peça para repetir a reposta até ter um valor correto. """ 

#Primeira pergunta
print("O relâmpago é visto antes de ser ouvido porque a velocidade da luz viaja mais rápido que a velocidade do som?")
print("[V / F] ?")
resp = input("--->>> ").strip().upper()

while resp not in 'VF': #loop para ter resposta adequada
    print("Por favor digite 'V' para verdadeiro e 'F' para falso.")
    resp = input("--->>> ").strip().upper()

    #verificar resposta 1
    if resp in 'V': 
        print("ESTÁ CERTO!\nProxima pergunta...\n")
    elif resp in 'F':
        print("ERROU!\n\n")

# Segunda pergunta
print("A água da privada gira em sentidos diferentes no hemisfério norte e no hemisfério sul.")
print("[V / F] ?")
resp = input("--->>> ").strip().upper()

#loop para ter resposta adequada
while resp not in 'VF':
    print("Por favor digite 'V' para verdadeiro e 'F' para falso.")
    resp = input("--->>> ").strip().upper()

    #validação de resposta
    if resp in 'V':
        print("ESTÁ CERTO!\nProxima pergunta...\n")
    elif resp in 'F':
        print("ERROU!\n\n")

# Início da terceira pergunta
print("Leva nove meses para um elefante nascer. ")
print("[V / F] ?")
resp = input("--->>> ").strip().upper()

while resp not in 'VF':
    print("Por favor digite 'V' para verdadeiro e 'F' para falso.")
    resp = input("--->>> ").strip().upper()

    if resp in 'F':
        print("ACERTOU!\nOs bebês elefantes nascem após 22 meses.\nVolte sempre!")
    elif resp in 'V':
        print("ERROU!")

