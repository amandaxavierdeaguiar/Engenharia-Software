""" Ex 23 - Tabuada com um número dado pelo usuário """

num = int(input('Digite o numero que deseja saber a tabuada:\n--->'))

for tabuada in range(0,10):
    print(num, 'X', tabuada + 1, '=', num * (tabuada + 1)) 

# + 1 caractere pois começa em Zero  
    