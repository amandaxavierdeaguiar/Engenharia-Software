import pandas as pd
from modelos.classes import Dados

def main():
    base_de_dados = 'C:\\Users\\\\amand\\Documents\\MeusProjetos\\engenharia_software\\Amanda_Aguiar\\AulasPythonAvancada\\Aulas\\#2 - PANDAS - Biblioteca\\imoveis.csv'

    analise = Dados(base_de_dados)

    print('Ler tabela completa')
    print(analise.dados)

    print('Ler inicio tabela')
    print(analise.ler_inicio(10))

    print('Ler final tabela')
    print(analise.ler_final(5))

    print('Ler tipo tabela')
    print(analise.ler_tipo())

    print('Ler colunas tabela')
    print(analise.ler_colunas())

    print('Ler colunas tabela')
    print(analise.tipo_dado_cabecalho('Cidade'))

    print('Ver media de rendas por tipo de imóvel')
    print(analise.media_rendas)

    print('Ver percentagem por tipo de imóvel')
    print(analise.percentagem_tipo())

    print('Mostrar valores nulos')
    print(analise.mostrar_valores_nulos())

    print('Remover valores nulos')
    print(analise.remover_valores_nulos(0))

    print('Mostrar valores nulos')
    print(analise.mostrar_valores_nulos())

    print('Encontrar valores a zero')
    print(analise.encontrar_valores_zero())

    print('Filtro de quartos')
    print(analise.filtro_quarto(1))

    print('Filtro de Aluguer')
    print(analise.filtro_aluguer(500))

    print('Filtro Quarto e Aluguer')
    print(analise.filtro_quarto_aluguer())

    print('Filtro Quarto 2, Aluguel 750€, Área maior que 70m2')
    print(analise.filtro_aluguel_tamanho())

    #analise.guardar('teste123.csv', separador= ';')

    print('Guardar coluna despesas mensais')
    print(analise.despesas_mensais())

    print('Guardar coluna despesas anuais')
    print(analise.despesas_anuais())
   

if __name__ == '__main__':
    main()