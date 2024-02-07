class Conta:
    def __init__(self, nib, titular, saldo, limite):
        self.nib = nib
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo (self):
        return self.__saldo
    
    def get_limite (self):
        return self.__limite
    
    def set_limite (self, valor):
        self.__limite = valor

conta = Conta("1234456", "Amanda", 100, 400)

conta.get_saldo()
print(f"Saldo da conta de Amanda é R$ {conta.get_saldo():.2f}")
conta.get_limite()
print(f"O limite {conta.get_limite}")
conta.set_limite()
print(f"Novo limite para a conta de Amanda é R$ {conta.set_limite():.2f}")


    
    
"""    def levantar(self, valor):
        if valor > self.__limite:
            print("O seu limite é de 400€ diários")
        else:
            if self.__saldo > valor:
                self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        print(f"A conta {self.identidade} tem {self.__saldo}€ disponíveis.")"""

    