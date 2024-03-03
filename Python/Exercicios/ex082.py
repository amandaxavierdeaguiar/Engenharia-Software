"""Crie uma classe chamada Produto que inclua atributos para o nome e a quantidade em stock. Utilize a property para aceder a quantidade em stock, garantindo que ela nunca seja negativa. Inclua um método mostrar_stock que exibe uma mensagem indicando quantas unidades do produto estão disponíveis. Adicione também um método adicionar_stock que permite aumentar a quantidade de stock de um produto."""

class Produto:
    def __init__(self, nome='', stock=0):
        self.nome = nome
        self.__stock = stock
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, qtde_estoque):
        if qtde_estoque >= 0:
            self.__stock = qtde_estoque
        else:
            print('Quantidade de estoque inválida!')
            
    def aumentar_stoque(self, qtde):
        self.stock += qtde
    
    def diminuir_estoque(self, qtde):
        if self.stock >= qtde:
            self.stock -= qtde   
        else:
            print('Não há quantidade de unidades no estoque')

# testando
livro = Produto(nome='Livro', stock=10)
print(livro.stock)  
livro.aumentar_stoque(5)
print(livro.stock)  
livro.diminuir_estoque(5)
print(livro.stock)  
livro.diminuir_estoque(15)
print(livro.stock)