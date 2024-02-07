""" Crie um programa com uma função chamada fatorial(), que receba dois parâmetros: o primeiro será o número a calcular o fatorial e o segundo será opcional e lógico que indique se será exibido no ecrã ou não o processo de cálculo do fatorial. """

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


# programa principal
numero = int(input("Insira um número para ver o seu fatorial: "))
opcao = input("Deseja ver o processo? [S/N]\n---> ").strip().lower()
mostra = True if opcao == "s" else False
resultado = fatorial(numero, mostra)
print(resultado)


