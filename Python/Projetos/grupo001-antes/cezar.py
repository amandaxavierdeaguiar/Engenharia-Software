import datetime


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\n\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar o número.\033[m")
            return None


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i, item in enumerate(lista, start=1):
        print(f"\033[33m{i}\033[m - \033[34m{item}\033[m")
    print(linha())
    return leiaInt("\033[33mSua Opção -> \033[m")


def arquivoExiste(nome):
    try:
        with open(nome, 'rt'):
            pass
        return True
    except FileNotFoundError:
        return False


def criarArquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass
        print('\033[32mO Arquivo foi criado com sucesso!\033[m')
    except Exception as e:
        print(f'\033[31mHouve um ERRO na criação do arquivo: {e}\033[m')


def duplicados(novo_livro, livros):
    return any(livro_encontrado['isbn'] == novo_livro['isbn'] for livro_encontrado in livros)


def adicionar(livros):
    while True:
        livro = {}
        livro["utilizador"] = input("Insira o seu nome --> ")
        livro["titulo_livro"] = input("Nome do Livro --> ")
        livro["autor"] = input("Autor ou autores --> ")
        livro["isbn"] = input("ISBN --> ")

        while len(livro['isbn']) != 13 or not livro['isbn'].startswith('978'):
            print("O ISBN tem que ter obrigatoriamente 13 dígitos e começar por '978'.")
            livro['isbn'] = input('ISBN: ')

        try:
            livro['ano'] = int(input('Ano de Publicação: '))
            if len(str(livro['ano'])) != 4:
                raise ValueError("O ano deve ter obrigatoriamente 4 dígitos.")
        except ValueError as e:
            print(f"Erro: {e}")
            return

        livro['editora'] = input("Nome da Editora: ")
        livro['categoria'] = input("Qual categoria? ")
        livro['disponibilidade'] = bool(int(input("Disponível? (1 para sim, 0 para não) ")))

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
                a.write(f'Título: {livro["titulo_livro"]}\n')
                a.write(f'Autor: {livro["autor"]}\n')
                a.write(f'ISBN: {livro["isbn"]}\n')
                a.write(f'Ano: {livro["ano"]}\n')
                a.write(f'Editora: {livro["editora"]}\n')
                a.write(f'Categoria: {livro["categoria"]}\n')
                a.write(f'Disponibilidade: {livro["disponibilidade"]}\n')
                a.write('----------\n')
            print(f'\033[32mNovo registro de livro adicionado com sucesso!\033[m')
    except Exception as e:
        print(f'Houve um erro na hora de escrever os dados: {e}')


def lerArquivo(nome):
    try:
        with open(nome, 'r') as a:
            print(a.read())
    except Exception as e:
        print(f'\033[31mErro ao ler arquivo: {e}\033[m')


def procurar_livro(livros):
    print("Livros Disponíveis:")
    for livro in livros:
        if livro['disponibilidade']:
            print(f"Nome do Livro: {livro['titulo_livro']}")
            print(f"Autor: {livro['autor']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"Editora: {livro['editora']}")
            print(f"Categoria: {livro['categoria']}")
            print("-----")


def emprestimo_devolucao(livros):
    utilizador = input("Insira o seu nome --> ")
    ref = input("Insira a referência que tiver do livro (titulo, autor, isbn) --> ")

    livro_encontrado = None
    for livro in livros:
        if ref.lower() in livro['titulo_livro'].lower() or ref.lower() in livro['autor'].lower() or ref == livro['isbn']:
            livro_encontrado = livro
            break

    if livro_encontrado is not None:
        print(f"Nome do Livro: {livro_encontrado['titulo_livro']}")
        print(f"Autor: {livro_encontrado['autor']}")
        print(f"ISBN: {livro_encontrado['isbn']}")
        print(f"Editora: {livro_encontrado['editora']}")
        print(f"Categoria: {livro_encontrado['categoria']}")
        print(f"Disponibilidade: {livro_encontrado['disponibilidade']}")
        confirmar = input("É este o livro que procura? [s/n] --> ").lower()

        if confirmar == 's':
            if livro_encontrado['disponibilidade']:
                emprestimo = input("Deseja realizar o empréstimo deste livro? [s/n] ? --> ").lower()
                if emprestimo == 's':
                    livro_encontrado['disponibilidade'] = False
                    print(f"Empréstimo realizado com sucesso a {utilizador}. Data do empréstimo: {datetime.datetime.now()}")
            else:
                devolucao = input("Deseja realizar a devolução deste livro? [s/n] ? --> ").lower()
                if devolucao == 's':
                    livro_encontrado['disponibilidade'] = True
                    print(f"Devolução realizada com sucesso de {utilizador}. Data da devolução: {datetime.datetime.now()}")
        else:
            print("Operação cancelada.")
    else:
        print("Livro não encontrado na base de dados.")


def atualizar_arquivo(arquivo, livros):
    try:
        with open(arquivo, 'w') as f:
            for livro in livros:
                f.write(f'Título: {livro["titulo_livro"]}\n')
                f.write(f'Autor: {livro["autor"]}\n')
                f.write(f'ISBN: {livro["isbn"]}\n')
                f.write(f'Ano: {livro["ano"]}\n')
                f.write(f'Editora: {livro["editora"]}\n')
                f.write(f'Categoria: {livro["categoria"]}\n')
                f.write(f'Disponibilidade: {livro["disponibilidade"]}\n')
                f.write('----------\n')
    except Exception as e:
        print(f'Houve um erro ao atualizar o arquivo: {e}')


def remover_livro(arquivo, livros):
    utilizador = input("Insira o seu nome --> ")
    ref = input("Insira a referência que tiver do livro (titulo, autor, isbn) --> ")

    livro_encontrado = None
    for livro in livros:
        if ref.lower() in livro['titulo_livro'].lower() or ref.lower() in livro['autor'].lower() or ref == livro['isbn']:
            livro_encontrado = livro
            break

    if livro_encontrado is not None:
        print(f"Nome do Livro: {livro_encontrado['titulo_livro']}")
        print(f"Autor: {livro_encontrado['autor']}")
        print(f"ISBN: {livro_encontrado['isbn']}")
        print(f"Editora: {livro_encontrado['editora']}")
        print(f"Categoria: {livro_encontrado['categoria']}")
        print(f"Disponibilidade: {livro_encontrado['disponibilidade']}")

        confirmar = input("É este o livro que procura? [s/n] --> ").lower()
        if confirmar == 's':
            if livro_encontrado["disponibilidade"]:
                devolvido = input("O livro está marcado como emprestado. Foi devolvido? [s/n] --> ").lower()
                if devolvido != 's':
                    print("Não é possível remover o livro enquanto estiver emprestado.")
                else:
                    livros.remove(livro_encontrado)
                    atualizar_arquivo(arquivo, livros)
                    print(f"O livro foi removido da base de dados por {utilizador}.")
            else:
                livros.remove(livro_encontrado)
                atualizar_arquivo(arquivo, livros)
                print(f"O livro foi removido da base de dados por {utilizador}.")
        else:
            print("Operação cancelada.")
    else:
        print("Livro não encontrado na base de dados.")


def atualizar_arquivo(arquivo, livros):
    try:
        with open(arquivo, 'w') as f:
            for livro in livros:
                f.write(f'Título: {livro["titulo_livro"]}\n')
                f.write(f'Autor: {livro["autor"]}\n')
                f.write(f'ISBN: {livro["isbn"]}\n')
                f.write(f'Ano: {livro["ano"]}\n')
                f.write(f'Editora: {livro["editora"]}\n')
                f.write(f'Categoria: {livro["categoria"]}\n')
                f.write(f'Disponibilidade: {livro["disponibilidade"]}\n')
                f.write('----------\n')
    except Exception as e:
        print(f'Houve um erro ao atualizar o arquivo: {e}')


def biblioteca():
    livros = []
    arquivo = "nhe.txt"

    while True:
        resposta = menu(["Adicionar livro", "Remover livro", "Listar livros", "Procurar livros", "Emprestar livros", "Sair do Sistema"])

        if resposta == 1:
            cabecalho("ADICIONAR LIVRO")
            livros = adicionar(livros)
            cadastrar(arquivo, livros)

        elif resposta == 2:
            cabecalho("REMOVER LIVRO")
            remover_livro("nhe.txt", livros)

        elif resposta == 3:
            cabecalho("LISTAR LIVROS")
            lerArquivo(arquivo)

        elif resposta == 4:
            cabecalho("PROCURAR LIVROS")
            procurar_livro(livros)

        elif resposta == 5:
            cabecalho("EMPRÉSTIMO/DEVOLUÇÃO LIVROS")
            emprestimo_devolucao(livros)

        elif resposta == 6:
            print("Saindo da Biblioteca. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

biblioteca()