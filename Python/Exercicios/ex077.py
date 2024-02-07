""" 
Crie uma classe ContaBancariacom atributos titular, saldo e limite. Adicione métodos para depositar() e sacar(), alterando o saldo da conta de acordo com a operação.
"""
class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, deposita):
        self.deposita = deposita
        self.saldo += self.deposita
        print("\033[32mDepósito realizado com sucesso!\033[m")

    def sacar(self, saque):
        self.saque = saque
        if (self.saque > self.saldo):
            print("\033[31mSaldo insuficiente!\033[m")
        elif (self.saque > self.limite):
            print(f"\033[31mExcede seu limite que é de {pessoa.limite}€\033[m")
        else:
            self.saldo -= self.saque
            print("\033[32mSaque realizado com sucesso!\033[m")

pessoa = ContaBancaria(input("Nome: "), float(input("Saldo: ")), float(input("limite: ")))

while True:

    operacoes = int(input("O que deseja realizar?\n[ 1 ] Saque\n[ 2 ] Depósito\n[ 3 ] Extrato\n[ 4 ] Sair\n"))

    if operacoes == 1:
        valor = float(input("Valor a ser sacado: "))
        pessoa.sacar(valor)
    elif operacoes == 2:
        valor_dep = float(input("Qual o valor a ser depositado? "))
        pessoa.depositar(valor_dep)
    elif operacoes == 3:
        print(f"Seu saldo é de {pessoa.saldo}")
    elif operacoes == 4:
        print("\033[32mSaindo do sistema!\033[m")
        break
    else:
        print("Operação inválida!")