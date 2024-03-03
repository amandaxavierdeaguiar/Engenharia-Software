""" Crie um simulador de crédito habitação simples e sem taxas, que solicite o nome, ano de nascimento, rendimentos mensais, despesas mensais, montante do crédito e prazo em anos, guardando tudo dentro de um dicionário. Calcule, acrescentando ao dicionário, a idade, o remanescente após despesas, quanto deverá pagar mensalmente pelo crédito e se o crédito foi aprovado sempre que o remanescente seja superior ao valor mensal do crédito. """

import datetime

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
renda_mensal = float(input("Digite seus rendimentos mensais: "))
despesas_mensais = float(input("Digite suas despesas mensais: "))
montante_credito = float(input("Digite o montante do crédito: "))
termo_credito = int(input("Digite o prazo do crédito em anos: "))

ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento

remanescente_mensal = renda_mensal - despesas_mensais

mensalidade_credito = montante_credito / (termo_credito * 12)

aprovado = remanescente_mensal > mensalidade_credito

informacoes_credito = {
        "nome": nome,
        "idade": idade,
        "renda_mensal": renda_mensal,
        "despesas_mensais": despesas_mensais,
        "montante_credito": montante_credito,
        "termo_credito": termo_credito,
        "remanescente_mensal": remanescente_mensal,
        "mensalidade_credito": mensalidade_credito,
        "aprovado": aprovado
    }

print(informacoes_credito)