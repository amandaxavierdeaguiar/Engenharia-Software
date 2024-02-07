import pandas as pd
from programa.classe import Dados


def main():
    bd= 'C:\\Users\\amand\\Documents\\MeusProjetos\\engenharia_software\\Amanda_Aguiar\\AulasPythonAvancada\\Exercicios\\Pandas\\Alunos_Exercicios.csv'

    ver = Dados(bd)

    print('--- LER MEDIA DOS ALUNOS ---')
    print(ver.media_alunos())

    print('--- SITUACAO ALUNOS ---')
    print(ver.situacao_alunos())

    print('--- SOMENTE OS APROVADOS ---')
    print(ver.aprovados())

    print('--- SOMENTE OS REPROVADOS ---')
    print(ver.reprovados())

    print('--- GUARDAR OS APROVADOS ---')
    print(ver.guardar('aprovados.csv', 'Aprovado'))

    print('--- GUARDAR OS REPROVADOS ---')
    print(ver.guardar('reprovados.csv', 'Reprovado'))

    print('--- GUARDAR TODOS ---')
    print(ver.guardar('todos.csv', todos=True))



if __name__ == '__main__':
    main()