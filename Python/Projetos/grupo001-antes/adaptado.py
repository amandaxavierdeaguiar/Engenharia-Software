def Livro(self, titulo, autor, isbn, ano, editora, categoria, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano
        self.editora = editora
        self.categoria = categoria
        self.disponibilidade = disponibilidade

def livros(self):
        self.livros = []

def adicionar_livro(self, titulo, autor, isbn, ano, editora, categoria, disponibilidade):
    novo_livro = Livro(titulo, autor, isbn, ano, editora, categoria, disponibilidade)
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
        print(f"ISBN: {livro.isbn}")
        print(f"Ano: {livro.ano}")
        print(f"Editora: {livro.editora}")
        print(f"Categoria: {livro.categoria}")
        print(f"Disponível:{livro.disponivel()}")
        print()

def procurar_livro(self, titulo):
    for livro in self.livros:
        if livro.titulo == titulo:
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Categoria: {livro.categoria}")
            return
    print("Livro não encontrado!")

"""def salvar_dados(self, arquivo):
    with open(arquivo, 'wb') as f:
        pickle.dump(self.livros, f)
    print("Dados salvos com sucesso!")

    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, 'rb') as f:
                self.livros = pickle.load(f)
                print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado!")"""

# Se não existir, vai criar.
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #Vai criar a pasta
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo\033[m')
    else:
        print('\033[32mO Arquivo foi criado com sucesso!\033[m')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler arquivo!\033[m')
    else:
        print(a.readlines())

def cadastrar(arquivo):
    try:
        with open(arquivo, 'at') as a:
            livros = adicionar_livro()
            a.write(str(livros))
 
        print(f'\033[32mNovo registro de livro adicionado com sucesso!\033[m')
    except:
        print('Houve um erro na hora de escrever os dados!')
 
arquivo = "g.txt"
 

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
        while True: 
            titulo = str(input('O nome completo do livro: '))
            autor  = str(input('Nome(s) do(s) autor(es) do livro: '))
            isbn = int(input('ISBN: '))
    
            while len(str(isbn)) != 13 or not str(isbn).startswith('978'):
                print("O ISBN tem que ter obrigatoriamente 13 dígitos e começar por '978'.")
                isbn = int(input('ISBN novamente: '))
            
            ano = int(input('Ano de Publicação: '))
 
            while len(str(ano)) != 4:
                print("O ano tem que ter obrigatoriamente 4 dígitos.")
                ano = int(input('Ano de Publicação: '))
 
            editora = str(input("Nome da Editora: "))
            categoria = str(input("Qual categoria?"))
            disponibilidade = bool(input("Disponível? (1 para sim, 0 para não) "))
 
            continuar = input('Deseja adicionar outro livro? (s/n)')
 
            if continuar.lower() != 's':
                break

            adicionar_livro(titulo, autor, isbn, ano, editora, categoria, disponibilidade)
    elif opcao == "2":
        titulo = input("Digite o título do livro a ser removido: ")
        remover_livro(titulo)
    elif opcao == "3":
        listar_livros()
    elif opcao == "4":
        titulo = input("Digite o título do livro a ser procurado: ")
        procurar_livro(titulo)
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

print("Saindo do programa...")