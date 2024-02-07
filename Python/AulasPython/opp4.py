class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def __str__(self):
        return (f"Titular: {self.titular}\nSaldo: {self.saldo}")
    
conta_pessoal = ContaBancaria("Amanda", 1500, 400)
print(conta_pessoal)