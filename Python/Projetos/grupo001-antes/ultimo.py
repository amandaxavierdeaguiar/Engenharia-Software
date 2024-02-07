#Criando o cabeçalho para reutilizar:
def linha(tam=42):
    return '-' * tam
 
def cabecalho(txt):
    print(linha())
    print(txt.center(42)) #Meio da tela
    print(linha())
 
#Funcao ler numero inteiro. Para reutilizar!
def leiaInt(msg):
    while True:
        try: # permite que você teste um bloco de código para erros.
            n = int(input(msg))
        except(ValueError, TypeError): #permite que você teste um bloco de código para erros.
            print("\n\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuário preferiu não digitar o número.\033[m")
            return 0
        else:
            return n
 
#Criando o Menu
def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1 #Contado começa em 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m") #Para cada item da lista vai colcocar um espaço.
        c += 1
        # O contador vai acrescentar sempre um
    print(linha())
    opc = leiaInt("\033[33mSua Opção -> \033[m")
    return opc
 
#Apenas para ver se arquivo de texto existe.
def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
   
# Se não existir, vai criar.
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #Vai criar a pasta
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo\033[m')
    else:
        print('\033[32mO Arquivo foi criado com sucesso!\033[m')
 
#Cria função para adicionar livros:

#Arrumando
def adicionar():
    livros = {}
    while True:
        
        livros['titulo'] = str(input('O nome completo do livro: '))
        livros['autor'] = str(input('Nome(s) do(s) autor(es) do livro: '))
        livros['isbn'] = int(input('ISBN: '))
 
        while len(str(livros['isbn'])) != 13 or not str(livros['isbn']).startswith('978'):
            print("O ISBN tem que ter obrigatoriamente 13 dígitos e começar por '978'.")
            livros['isbn'] = int(input('ISBN: '))
 
        livros['ano'] = int(input('Ano de Publicação: '))
 
        while len(str(livros['ano'])) != 4:
            print("O ano tem que ter obrigatoriamente 4 dígitos.")
            livros['ano'] = int(input('Ano de Publicação: '))
 
        livros['editora'] = str(input("Nome da Editora: "))
        livros['categoria'] = str(input("Qual categoria?"))
        livros['disponibilidade'] = bool(input("Disponível? (1 para sim, 0 para não) "))
 
        #lista.append(livros)
 
        continuar = input('Deseja adicionar outro livro? (s/n)')
 
        if continuar.lower() != 's':
            break
 
    return livros
 
#Cadastrar novos livros
def cadastrar(arquivo):
    try:
        with open(arquivo, 'at') as a:
            livros = adicionar()
            #a.write(str(livros) + '\n')
            a.write(livros + '\n')
 
        print(f'\033[32mNovo registro de livro adicionado com sucesso!\033[m')
    except:
        print('Houve um erro na hora de escrever os dados!')
 
#Função para ler arquivo.
 
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler arquivo!\033[m')
    else:
        print(a.readlines())

def bonito(arquivo):
    for k, v in arquivo.items():
        print(f"{k} = {v}")
 
#Criando o nome do arquivo txt.
arquivo = "grupo001.txt"
 
#Puxar a função e criar arquivo.
if arquivoExiste(arquivo):
    print('Arquivo Encontrado com sucesso!')
else:
    print('Erro ao encontrar o arquivo!')
    criarArquivo(arquivo)
 
 
cabecalho("SISTEMA BIBLIOTECÁRIO")
 
while True:
 
    resposta = menu(["Adicionar livro", "Remover livro", "Listar livros", "Procurar livros","Emprestar livros", "Sair do Sistema"])
 
    if resposta == 1:
        cabecalho("ADICIONAR LIVRO")
        cadastrar(arquivo)
   
    elif resposta == 3:
        #Opção de Listar o conteúdo de um arquivo.
        #lerArquivo(arquivo)
        bonito(arquivo)
 
 
    elif resposta == 6:
        #Sair do Sistema.
        print("\033[32m\nSaindo do programa, até logo!\33[m")
        break
   
    else:
        #Caso não esteja na opção correta.
        print("\033[31mERRO! Digite uma opção válida\33[m")
