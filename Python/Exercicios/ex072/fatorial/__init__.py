def fatorial(num, mostrar=False):
    """
    Função para calcular o fatorial de um número.
    
    :param num: int, número para o qual o fatorial será calculado.
    :param mostrar: bool, opcional. Se True, exibe o processo de cálculo.
    :return: int, o valor do fatorial do número.
    """
    fat = 1
    for i in range(num, 0, -1):
        if mostrar:
            if i == 1:
                print(f"{i} = ", end="")
            else:
                print(f"{i} x ", end="")
        fat *= i
    return fat





