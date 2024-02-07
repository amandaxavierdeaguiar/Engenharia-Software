class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.identidade = identidade
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def levantar(self, valor):
        if valor > self.limite:
            print("O seu limite é de 400€ diários")
        else:
            if self.saldo > valor:
                self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"A conta {self.identidade} tem {self.saldo}€ disponíveis.")

    