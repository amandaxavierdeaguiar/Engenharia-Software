# Crie um programa que leia 5 notas introduzidas pelo utilizador e calcule a média aritmética entre eles:

print('Média\n'.center(30))
nota1 = float(input('Digite a primeiro nota:'))
nota2 = float(input('Digite a segundo nota:'))
nota3 = float(input('Digite a terceiro nota:'))
nota4 = float(input('Digite a quarto nota:'))
nota5 = float(input('Digite a quinto nota:'))

media = ((nota1 + nota2 + nota3 + nota4 + nota5)/5)
print(f"O valor da média é de {media}") 
