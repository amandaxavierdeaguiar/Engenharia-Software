class Conta:
    def __init__ (self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo
        self.limite = limite

    @property
    def saldo(self):
        return f'O saldo da conta é {self.__saldo}€' 
    
    @saldo.setter
    def saldo(self, valor):
        if valor > 1000:
            print('Valor não permitido') 
        else:
            self.__saldo = valor
            print('Saldo modificado com sucesso!')

conta = Conta("Amanda", 1250, 400)

