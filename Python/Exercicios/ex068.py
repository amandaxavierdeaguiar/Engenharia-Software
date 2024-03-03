""" Crie um programa com uma função que vai receber várias notas de alunos e vai retornar um dicionário com o seguinte: 
a)Quantidade de notas 
b)A maior nota 
c)A média da turma 
d)A situação (lógico opcional) >12 –boa <9,5 –fraca >9,5 e <12 -razoável """

# Crie um programa com uma função que vai receber várias notas de alunos e vai retornar um dicionário com o seguinte:
# a)Quantidade de notas
# b)A maior nota
# c)A média da turma
# d)A situação (lógico opcional) >12 –boa <9,5 –fraca >9,5 e <12 -razoável

def analisar_turma(notas):
    # Inicializa uma lista vazia para armazenar os dicionários de notas
    lista = []

    # Loop para adicionar cada nota ao dicionário e à lista
    for nota in notas:
        notas_dic = {"quantidade": 0, "maior": None, "media": 0, "situacao": ""}

        # Adiciona a nota ao dicionário e atualiza a quantidade de notas
        notas_dic['quantidade'] += 1

        # Atualiza a maior nota se necessário
        if notas_dic['maior'] is None or notas_dic['maior'] < nota:
            notas_dic['maior'] = nota

        # Atualiza a soma das notas
        notas_dic['media'] += nota

        # Calcula a média da turma
        notas_dic['media'] = notas_dic['media'] / notas_dic['quantidade']

        # Define a situação da turma
        if notas_dic['media'] > 12:
            notas_dic['situacao'] = 'Boa'
        elif 9.5 <= notas_dic['media'] < 12:
            notas_dic['situacao'] = 'Razoável'
        else:
            notas_dic['situacao'] = 'Fraca'

        # Adiciona o dicionário à lista
        lista.append(notas_dic.copy())

    return lista

# Testando a função com uma lista de notas
notas = []
nota = -1

while True:
    nota = float(input("Digite a nota [Digite -1 para sair]: "))

    if nota < 0:
        break

    notas.append(nota)

# Chama a função com a lista de notas
resultado = analisar_turma(notas)

# Imprime o resultado
for res in resultado:
    print(f"Quantidade de notas: {res['quantidade']}")
    print(f"Maior nota: {res['maior']}")
    print(f"Média da turma: {res['media']}")
    print(f"Situação: {res['situacao']}")
    print()
