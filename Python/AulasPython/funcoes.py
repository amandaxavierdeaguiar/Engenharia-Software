""" Interactive Help - informacoes sobre os modulos, classes, funcoes e outros aspectos.
uma ajuda #help(print)

Documentacao da funções(metodos) - docstring  - Explicar para o que serve
assinatura da função  - Que parametros ela leva
informacoes adicionais - pode mostrar a lista de metodos disponiveis. 

Docstrings -> """ """ Usadas para documentar o codigo. Coloque a seguir a função.
Ex: def soma(a, b)
    """ 
"""-> Calcula e imprime a soma de dois números. 
    param: a- primeiro numeros
    param: b- segundo numeros
    return: sem retorno"""
"""
        print(a+b)    
        
        """


""" 
Parametros opcionais - Se tiver alguma ausencia de parametro, a funcao nao roda.
def soma(a, b, c=0):
    print(a+b+c)

soma(2,4,6)

"""

""" 
Escopo  - 
def escopo(b):
    #identado - cria um escopo local (dentro do bloco que esta a definir)
    b+=5
    c=3
    print(f"A dentro vale {a}") 
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

#escopo global
a=6 
escopo(a)

"""


""" 
Retorno de resultados - 
return :  Nao pode ser integradas com outras funcoes
Nao pode ser usada como parametro para outra funcao
Pode retornar string, boolean, soma... 




 """
 


