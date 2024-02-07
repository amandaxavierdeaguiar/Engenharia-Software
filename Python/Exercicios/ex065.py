""" Crie um programa que tenha uma função que vai receber como parâmetro o ano de nascimento de uma pessoa e que retorne se a pessoa já pode tirar a carta de condução, se precisa de autorização do encarregado de educação ou se não pode. +18 anos –pode-16 anos –não pode-18 e +16 –com autorização """


from datetime import datetime

def carta_conducao(ano_nascimento):
    data_atual = datetime
    idade = data_atual.now().year - ano_nascimento

    if idade >= 18:
        return f"Com {idade} anos, você é maior de idade e PODE tirar a carta de condução"
    if idade < 16:
        return f"Com {idade} anos, você NÃO pode tirar a carta de condução"
    elif idade >= 16:
        return f"Com {idade} anos, você PODE tirar a carta de condução com AUTORIZAÇÃO!"
    

ano_nascimento = int(input("Digite seu ano de nascimento: "))
print(carta_conducao(ano_nascimento))
