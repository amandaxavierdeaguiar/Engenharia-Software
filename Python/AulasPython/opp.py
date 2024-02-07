"""
Criar uma conta bancaria
identidade, titular, saldo, limite
levantar dinheiro, depositar dinheiro, extrato.
"""

"""contas = list()

while True:
    conta = {"identidade": input("ID: "), 
            "titular" : input("Nome: "), 
            "saldo" : float(input("Saldo")), 
            "limite" : float(input("Saldo"))
            }
    contas.append(conta)
    resp = input("\nDeseja criar outra conta? [S/N]")
    if resp in 'Nn':
        break

print(contas)"""

def levantar_dinheiro(valor):
    if conta["saldo"] > valor:
        conta["saldo"] -= valor

def depositar_dinheiro(valor):
    conta["saldo"] += valor

def extrato():
    print(f"\n--- A conta {conta['identidade']} tem o saldo de {conta['saldo']}")

conta = {"identidade": input("ID: "), 
        "titular" : input("Nome: "), 
        "saldo" : float(input("Saldo")), 
        "limite" : float(input("limite"))
        }

print("Extrato")
extrato()
print("Deposito de 1000")
depositar_dinheiro(1000)
print("Extrato")
extrato()
print("Levantar 1000")
levantar_dinheiro(1000)
print("Extrato")
extrato()
levantar_dinheiro(400)
print("Extrato")
extrato()

