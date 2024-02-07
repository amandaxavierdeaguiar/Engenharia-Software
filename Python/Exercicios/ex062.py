def pauta(nome, lista_notas):
    print(f"Pauta do aluno {nome.upper()}")
    soma_notas = 0
    for notas in lista_notas:
        soma_notas += notas

    media = soma_notas / len(lista_notas)
    situacao = "Aprovado" if media <=9.5 else "Reprovado"
    print(f"Media {media:.2f}")
    print(f"Situação {situacao}")
 
nome = input("Digite o nome do Aluno: ")
notas = list()
contador = 0
while True:
    nota = float(input(f"Informe a {contador + 1}ª Nota: "))
    notas.append(nota)
    contador += 1 
    opcao = input("Deseja continuar? [S/N]").lower().strip()
    if opcao == "n":
        break
pauta(nome, notas)
