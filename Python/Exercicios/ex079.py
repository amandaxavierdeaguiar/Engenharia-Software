class ContaBancaria: 
    def __init__(self):
        self.__nib = "NIB"
        self.__titular = "Titular"
        self.__saldo = "Saldo"
        self.__limite = "Limite"

    def get_nib(self):
        return self.__nib
    
    def set_nib(self, nib):
        self.__nib = nib

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite

nib = int(input("Qual seu NIB? "))
titular = input("Nome do titular da conta:")
saldo = float(input("Informe o saldo inicial:"))
limite = float(input("Qual o seu limite? "))

conta = ContaBancaria()

conta.set_nib(nib)
conta.set_titular(titular)
conta.set_saldo(saldo)
conta.set_limite(limite)


print(f'Conta Criada com sucesso!\n{conta.get_nib()}, {conta.get_titular()}, {conta.get_saldo()}, {conta.get_limite()}')


    

    


    

    

    