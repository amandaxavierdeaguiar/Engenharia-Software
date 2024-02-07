import pickle

class Livro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, categoria):
        novo_livro = Livro(titulo, autor, categoria)
        for livro in self.livros:
            if livro.titulo == titulo:
                print("Livro já existe!")
                return
        self.livros.append(novo_livro)
        print("Livro adicionado com sucesso!")

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print("Livro removido com sucesso!")
                return
        print("Livro não encontrado!")

    def listar_livros(self):
        if len(self.livros) == 0:
            print("Não existem livros na biblioteca!")
            return
        for livro in self.livros:
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Categoria: {livro.categoria}")
            print()

    def procurar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Categoria: {livro.categoria}")
                return
        print("Livro não encontrado!")

    def salvar_dados(self, arquivo):
        with open(arquivo, 'wb') as f:
            pickle.dump(self.livros, f)
        print("Dados salvos com sucesso!")

    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, 'rb') as f:
                self.livros = pickle.load(f)
                print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado!")

biblioteca = Biblioteca()

while True:
    print("===== MENU =====")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Listar livros")
    print("4. Procurar livro")
    print("5. Salvar dados")
    print("6. Carregar dados")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        categoria = input("Digite a categoria do livro: ")
        biblioteca.adicionar_livro(titulo, autor, categoria)
    elif opcao == "2":
        titulo = input("Digite o título do livro a ser removido: ")
        biblioteca.remover_livro(titulo)
    elif opcao == "3":
        biblioteca.listar_livros()
    elif opcao == "4":
        titulo = input("Digite o título do livro a ser procurado: ")
        biblioteca.procurar_livro(titulo)
    elif opcao == "5":
        arquivo = input("Digite o nome do arquivo para salvar os dados: ")
        biblioteca.salvar_dados(arquivo)
    elif opcao == "6":
        arquivo = input("Digite o nome do arquivo para carregar os dados: ")
        biblioteca.carregar_dados(arquivo)
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

print("Saindo do programa...")