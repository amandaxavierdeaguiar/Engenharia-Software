""" Crie um programa que pergunte a quantidade de km percorridos por um carro alugado 
e quantidade de dais que foi alugado. 
Apresente o total a pagar sabendo que o carro custa 60€ dia e 0.456€/km """


quantidade_km = float(input('Quantos km foram percorridos? '))
valor_km = (quantidade_km * 0.456)

quantidade_dias = int(input('Quantos dias alugou? '))
valor_dia = 60
valor_dias = (quantidade_dias * valor_dia)

valor_total_pagar = (valor_km + valor_dias)

print(f'O valor pago em relação a km é de {valor_km} €')
print(f'O valor somado da quantidade de dias é de  {valor_dias} €\n')

print(f'O valor total a pagar é de {valor_total_pagar} €')
