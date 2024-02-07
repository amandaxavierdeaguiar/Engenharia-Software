""" 
Desenvolver um sistema em Python para gerir os livros de uma biblioteca. O sistema permitirá adicionar, remover, listar e procurar livros, além de gerir empréstimos(opcional).    
Grupo: Amanda Xavier, Jandira Pedrosa, Cesar Maia e João Barbieri 
"""

def cabecalho(txt):
    """ 
    Imprime o cabeçalho
    :param: txt
    :return: no return
    """
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)

def menu(lista):
    """
    Mostra o menu principal
    :param lista: opções do menu
    :return: no return
    """
    cabecalho("MENU PRINCIPAL")
    c = 1
    #Sistema de cores no console - \033[33m(Cor) e tem que fechar com \033[m 
    for item in lista: #Cada cada item na lista de menu, será enumerado! 
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m") 
        c += 1 
    print('-' * 40)
    opc = int(input("\033[33mSua Opção -> \033[m"))
    return opc

def duplicados(novo_livro, livros):
    """
    Confirmar se existem ou não livros duplicados no arquivo
    :param novo_livro: número de ISBN
    :param livros: número de ISBN
    :return:
    """
    return any(
        livro_encontrado['isbn'] == novo_livro['isbn']
        for livro_encontrado in livros
    )

def adicionar(livros):
    """
    Adiciona novos livros ao arquivo
    :param livros: titulo, autor, isbn, ano, editora, categoria, disponibilidade
    :return: livros
    """
    while True:
        livro = {}

        livro['titulo'] = input('O nome completo do livro: ')
        livro['autor'] = input('Nome(s) do(s) autor(es) do livro: ')
        livro['isbn'] = input('ISBN: ')
        
        while len(livro['isbn']) != 13 or not livro['isbn'].startswith('978'):
            print("O ISBN tem que ter obrigatoriamente 13 dígitos e começar por '978'.")
            livro['isbn'] = input('ISBN: ')

        livro['ano'] = input('Ano de Publicação: ')

        while len(livro['ano']) != 4:
            print("O ano tem que ter obrigatoriamente 4 dígitos.")
            livro['ano'] = input('Ano de Publicação: ')

        livro['editora'] = input("Nome da Editora: ")
        livro['categoria'] = input("Qual categoria? ")
        livro['disponibilidade'] = bool(input("Disponível? (1 para sim, 0 para não) "))

        if not duplicados(livro, livros):
            livros.append(livro)
            print("Livro adicionado com sucesso.")
        else:
            print("Este livro já existe.")
        

        continuar = input('Deseja adicionar outro livro? (s/n)')

        if continuar.lower() != 's':
            break

    return livros

def cadastrar(arquivo, lista):
    """
    Cadastra um livro no arquivo
    :param arquivo: livros
    :param lista: titulo, autor, isbn, ano, editora, categoria, disponibilidade
    :return: arquivo
    """
    """with garante que o arquivo será fechado automaticamente depois que o bloco recuado de código for executado."""
    try: #'a' - append (Para adicionar no arquivo txt) 
        with open(arquivo, 'a') as a: 
            for livro in lista:
                a.write(f'Título: {livro["titulo"]}\n')
                a.write(f'Autor: {livro["autor"]}\n')
                a.write(f'ISBN: {livro["isbn"]}\n')
                a.write(f'Ano: {livro["ano"]}\n')
                a.write(f'Editora: {livro["editora"]}\n')
                a.write(f'Categoria: {livro["categoria"]}\n')
                a.write(f'Disponibilidade: {livro["disponibilidade"]}\n')
                a.write('----------\n')
                print(f'\033[32mNovo registro de livro adicionado com sucesso!\033[m')
    except:
        print('Houve um erro na hora de escrever os dados!')


def lerArquivo(nome):
    """
    Ler e imprimir o conteúdo do arquivo
    :param nome: nome do livro
    :return: arquivo
    """
    """'r' - significa read para ler o arquivo"""
    try:
        with open(nome, 'r') as a:
            print(a.read())
    except:
        print('\033[31mErro ao ler arquivo!\033[m')


def remover_livro(arquivo):
    """
    Remove um livro do arquivo pedindo várias informações ao utilizador
    :param arquivo: título, isbn, ano, autor, editora, categoria, disponibilidade
    :return: arquivo
    """
    # Obter input do utilizador para a informação ser removida

    titulo = input("Digite o título do livro que deseja remover: ")
    isbn = input("Qual ISBN para apagar: ")
    ano = input("Ano:")
    autor = input("Qual autor para apagar: ")
    editora = input("Qual editora para apagar: ")
    categoria = input("Qual categoria para apagar: ")
    disponibilidade = input("Qual disponibilidade para apagar: ")

    try:
        with open(arquivo, 'r') as r:
            linhas = r.readlines()
        with open(arquivo, 'w') as w:
            for linha in linhas:
                # só escreve a linha se ela não tiver nenhum dos campos
                if titulo not in linha and isbn not in linha and ano not in linha and autor not in linha and editora not in linha and categoria not in linha and disponibilidade not in linha:
                    w.write(linha)
        print("\033[32mLivro removido com sucesso!\033[m")
    except:
        print('\033[31mErro ao remover o livro!\033[m')

def procurar_livro(arquivo):
    """
    Procura um livro através do título
    :param arquivo: título
    :return: arquivo
    """
    titulo = input("Digite o título do livro que deseja procurar: ").strip()

    try:
        with open(arquivo, 'r') as r:
            livros = r.readlines()

        livro_encontrado = False
        for linha in livros:
            if titulo in linha:
                livro_encontrado = True
                print("\033[32mLivro encontrado:\033[m")
                print(linha, end='')

        if not livro_encontrado:
            print("\033[31mLivro não encontrado!\033[m")

    except FileNotFoundError:
        print("\033[31mErro ao ler arquivo!\033[m")

# Criação do arquico de txt
arquivo = "livro.txt"

while True:
    resposta = menu(["Adicionar livro", "Remover livro", "Listar livros", "Procurar livros", "Sair do Sistema"])

    if resposta == 1:
        cabecalho("ADICIONAR LIVRO")
        livros = adicionar([])
        cadastrar(arquivo, livros)

    if resposta == 2:
        cabecalho("REMOVER LIVRO")
        remover_livro(arquivo)

    elif resposta == 3:
        cabecalho("LIVROS CADASTRADOS")
        lerArquivo(arquivo)
    
    elif resposta == 4:
        cabecalho("PROCURAR POR DISPONIBILIDADE")
        procurar_livro(arquivo)

    elif resposta == 5:
        # Sair do Sistema.
        print("\033[32m\nSaindo do programa, até logo!\33[m")
        break