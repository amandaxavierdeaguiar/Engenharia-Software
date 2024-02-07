"""def escopo(b):
    #identado - cria um escopo local (dentro do bloco que esta a definir)
    global a #Variavel dentro do escopo global
    a = 8 #A global vai começar a valer 8.
    b += 5
    c = 3
    print(f"A dentro vale {a}") 
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

#escopo global
a=6 
escopo(a)
print(f"A fora vale {a}")"""

def soma(a = 0, b = 0, c = 0):
    """_summary_

    Args:
        a (int, optional): _description_. Defaults to 0.
        b (int, optional): _description_. Defaults to 0.
        c (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """
    s = a + b + c
    return s

resultado = soma(c=2, a=1, b=3)
resultado2 = soma(75, 45, 52)
print(resultado)
print(resultado2)