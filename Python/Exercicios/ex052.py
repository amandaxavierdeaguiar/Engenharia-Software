""" Crie um programa que leia o nome e a média de um aluno, calculando a sua situação, tudo dentro de um dicionário. No final mostre todo o conteúdo do dicionário. 
Situação: 
Média >= 9,5 – Aprovado 
Média < 9,5 - Reprovado """

dados = dict()
lista = list()

while True:
    dados['nome'] = str(input('Digite o nome do aluno:'))
    dados['media'] = float(input(f'Digite a média da(o) {dados["nome"]}:'))
    dados["situação"] = "Aprovado" if dados["media"] >= 9.5 else "Reprovado"

    lista.append(dados.copy())
    print(dados)

    continuar = str(input('Deseja continuar?[S/N]')).lower()

    if continuar != 's':
        print("\n--- Lista de Alunos ---\n")
        for e in lista:
            for k in e.items():
                print(k)
        break

