""" Ex 16 - Crie um programa que leia a média que leia 5 notas de um aluno e calcule a sua média
>= 9.5 passou
> 8 e < 9.5  em recuperacao
<8 reprova
"""

nota = float(input("Digite a nota 1 = "))
nota2 = float(input("Digite a nota 2 = "))
nota3 = float(input("Digite a nota 3 = "))
nota4 = float(input("Digite a nota 4 = "))
nota5 = float(input("Digite a nota 5 = "))

media = ((nota + nota2 + nota3 + nota4 + nota5) / 5)

print(f"A sua média é de {media:.2f}")

if media >= 9.5:
    print("Aprovado")
elif media >= 8 and media < 9.5:
    print("Em recuperacao")
else:
    print("Reprova")
    