def cabecalho(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print('-' * 40)
    opc = int(input("\033[33mSua Opção -> \033[m"))
    return opc

def duplicados(novo_livro, livros):
    return any(
        livro_encontrado['isbn'] == novo_livro['isbn']
        for livro_encontrado in livros
    ) #Duplicados nao esta funcionando!

def adicionar(livros):
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
    try:
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
    try:
        with open(nome, 'r') as a:
            print(a.read())
    except:
        print('\033[31mErro ao ler arquivo!\033[m')


def remover_livro(arquivo):
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


arquivo = "livros.txt"

while True:
    resposta = menu(["Adicionar livro", "Remover livro", "Listar livros", "Procurar livros","Emprestar livros", "Sair do Sistema"])

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

    elif resposta == 6:
        # Sair do Sistema.
        print("\033[32m\nSaindo do programa, até logo!\33[m")
        break