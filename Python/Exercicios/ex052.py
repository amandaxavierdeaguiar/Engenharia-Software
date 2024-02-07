""" Crie um programa que leia o nome e a média de um aluno, calculando a sua situação, tudo dentro de um dicionário. No final mostre todo o conteúdo do dicionário. 
Situação: 
Média >= 9,5 – Aprovado 
Média < 9,5 - Reprovado """

dados = dict()
lista = list()

while True:
    dados['nome'] = str(input('Digite o nome do aluno:'))
    dados['media'] = int(input(f'Digite a média da(o) {dados["nome"]}:'))
    lista.append(dados.copy())
    continuar = str(input('Deseja continuar?[S/N]')).lower()

    while continuar != 's':
        for e in lista:
            for k, v in e.items():
                if dados['media'] >= 9.5:
                    dados['situacao'] = 'Aprovado'
                    print(f"O aluno {dados['nome']}, teve a média {dados['media']} e sua situação é {dados['situacao']}")    
                    break
                           
                elif dados['media'] < 9.5:
                    dados['situacao'] = 'Reprovado'
                    print(f"O aluno {v}, teve a média {k} e sua situação é {dados['situacao']}")
                    break                 
        break

