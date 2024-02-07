from function import *

while True:
    try:
        titulo_livro =  input('Titulo: ') 
        if not titulo_livro:
            print('O Título não pode ser uma string vazia')
            continue
        autor_livro = titulo_livro.strip().capitalize()
        break
    except Exception as e:
        print(f'Erro: {e}')

while True:
    try:
        autor_livro =  input('Autor: ') 
        if not autor_livro:
            print('Autor não pode ser uma string vazia')
            continue
        autor_livro = autor_livro.strip().capitalize()
        break
    except Exception as e:
        print(f'Erro: {e}')

while True:
    try:
        ano_livro = int(input('Ano: '))
        if ano_livro < 1900 or ano_livro > 2024:
            print('O ano tem que ser entre 1900 e o ano atual')
            continue
        break
    except ValueError:
        print('Ano tem que ser um número')
    except Exception as e:
        print(f'Erro: {e}')

livro = Livro(titulo_livro, autor_livro, ano_livro)
print(livro)
