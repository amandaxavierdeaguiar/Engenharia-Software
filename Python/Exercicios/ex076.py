""" Crie uma classe Produto com os atributos nome e quantidade em stock. Adicione um método que mostre o stock no estilo “O produto X tem Y unidades em stock”. Adicione um novo método que aumenta a quantidade de stock numa determinada quantidade. """

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade_stock = quantidade
        
    def stock(self):
        print(f"O produto {self.nome} tem {self.quantidade_stock} unidades em stock")
    
    def aumentar_stock(self, quantidade):
        self.quantidade_stock += quantidade

prod1 = Produto("Hamburguer de Salmão" , 35)
prod1.stock()
prod1.aumentar_stock(10)
prod1.stock()

prod2 = Produto("Hamburguer de Picanha" , 35)
prod2.stock()
prod2.aumentar_stock(5)
prod2.stock()

prod3 = Produto("Pão de Hamburguer", 48)
prod3.stock()
prod3.aumentar_stock(60)
prod3.stock()
