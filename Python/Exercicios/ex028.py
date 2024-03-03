""" Crie um jogo que faça 3 perguntas ao utilizado e que apenas aceite resposta V ou F. Caso esteja errado, peça para repetir a reposta até ter um valor correto. """ 

print("Jogo das perguntas!")
resp = input("Digite [ V ] para jogar\n--->>> ").strip().upper()

while resp in 'V':
        #Primeira Pergunta:
        print("O relâmpago é visto antes de ser ouvido porque a velocidade da luz viaja mais rápido que a velocidade do som?")
        print("[V / F] ?")
        resposta = input("--->>> ").strip().upper()
        if resposta == 'F':
            print("Tente novamente!")
            continue
        elif resposta == 'V':
            print("Você acertou! Parabéns.")
            break
        
print("Proxima Pergunta... ")
resps = input("Digite [ V ] para jogar\n--->>> ").strip().upper()

while resps in 'V':      
    #Segunda Pergunta:
    print("A água da privada gira em sentidos diferentes no hemisfério norte e no hemisfério sul.")
    print("[V / F] ?")
    respost = input("--->>> ").strip().upper()
    
    if respost == 'V':
        print("Você acertou! Parabéns.")
        break
    elif respost == 'F':
        print("Tente novamente!")
        continue
    
        
print("Última Pergunta... ")
respos = input("Digite [ V ] para jogar\n--->>> ").strip().upper()

while respos in 'V':         
    #Terceira pergunta
    print("Leva nove meses para um elefante nascer. ")
    print("[V / F] ?")
    respo = input("--->>> ").strip().upper()
    
    if respo in 'V':
        print("ERROU!")
        continue
    elif respo in 'F':
        print("ACERTOU!\nOs bebês elefantes nascem após 22 meses.\n")
        break

print("Foi ótimo jogar consigo!\nVolte sempre!")
    
        