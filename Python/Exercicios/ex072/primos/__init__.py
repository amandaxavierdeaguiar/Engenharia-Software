# Numero primo - Apenas pode ser divido por ele mesmo ou pelo numero 1 

def primos(num):
    tot = 0 # Variável de controle

    for i in range(1, num + 1):
        if num % i == 0:
            tot += 1 # mesmo que tot = tot + 1

    if tot == 2:
        return(f'O número {num} é PRIMO! Foi divisível {tot} vezes')
    else:
        return(f'O número {num} NÃO É PRIMO! Foram divisíveis {tot} vezes')