"""Modifique o exercício 77 para ter atributos privados para titular, saldo e limite. Implemente getters e setters usando property para esses atributos. Adicione métodos para depositar() e sacar(), que devem alterar o saldo da conta. Garanta que as operações respeitem o limite da conta e que o saldo não se torne negativo."""

class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # Setters
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("Saldo não pode ser negativo")
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        if limite < 0:
            raise ValueError("Limite não pode ser negativo")
        self.__limite = limite

    def depositar(self, deposita):
        self.saldo += deposita
        print("\033[32mDepósito realizado com sucesso!\033[m")

    def sacar(self, saque):
        if (saque > self.__saldo):
            print("\033[31mSaldo insuficiente!\033[m")
        elif (saque > self.__limite):
            print(f"\033[31mExcede seu limite que é de {self.__limite}€\033[m")
        else:
            self.__saldo -= saque
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