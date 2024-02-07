"""Ex14 - Crie um programa que leia um número inteiro introduzido pelo utilizadfor e que simule um radar de velocidade.
  > 80 km/h multado 
  <= 80km/h não multado """

velocidade = int(input("Digite a Quilometragem: "))
velocidade_acima = (velocidade - 80) * 7
total = velocidade_acima + 100

if velocidade > 80:
    print('Velocidade acima do permitido!')
    print(f'Recebeu a multa de: 100€ + {velocidade_acima}€ por cada km acima do permitido. O total do valor a pagar é de: {total}€')
else:
    print('Não receberá multa.')
    