import pandas as pd

class Dados:
    def __init__(self, dados):
        self.dados = pd.read_csv(dados, sep= ',')

    """@property
    def dados(self):
        return self.dados"""


    def media_alunos(self):
        self.dados['Media Aluno'] = (self.dados['Exercício 1'] + self.dados['Exercício 2'] + self.dados['Exercício 3'] + self.dados['Exercício 4'] + self.dados['Exercício 5']) / 5
        return self.dados

    
    def situacao_alunos(self):
        self.dados['Situacao'] = 'Reprovado'  # inicia por Reprovado
        self.dados.loc[self.dados['Media Aluno'] >= 9.5, 'Situacao'] = 'Aprovado' #loc - função localiza os valores 
        return self.dados
    
    def aprovados(self):
        aprovado = self.dados['Situacao'] == 'Aprovado'
        return self.dados[aprovado]
        
    def reprovados(self):
        reprovado = self.dados['Situacao'] == 'Reprovado'
        return self.dados[reprovado]
    
    """def guardar(self, nome_arquivo, situacao, separador = ';'):
    #UTF-8-sig permite acento das palavras SIG - força a utilizacao
    #Separador sep= ';'
    #decidir o que guardar
        if situacao == 'Aprovado':
            df_para_guardar = self.aprovados()
        elif situacao == 'Reprovado':
            df_para_guardar = self.reprovados()
        else:
            df_para_guardar = self.dados

        #guardar o que foi decidido acima
        df_para_guardar.to_csv(nome_arquivo, index=False, sep=separador, encoding='UTF-8-sig')
        #Tem que especificar o nome do arquivo.
        print(f'{nome_arquivo}Arquivo Criado com sucesso!')"""
    
    def guardar(self, nome_arquivo, situacao=None, todos=False, separador = ';'):
        #UTF-8-sig permite acento das palavras SIG - força a utilizacao
        #Separador sep= ';'
        #decidir o que guardar
        if todos:
            df_para_guardar = self.dados
        elif situacao == 'Aprovado':
            df_para_guardar = self.aprovados()
        elif situacao == 'Reprovado':
            df_para_guardar = self.reprovados()
        else:
            df_para_guardar = self.dados

        #guardar o que foi decidido acima
        df_para_guardar.to_csv(nome_arquivo, index=False, sep=separador, encoding='UTF-8-sig')
        #Tem que especificar o nome do arquivo.
        print(f'{nome_arquivo}Arquivo Criado com sucesso!')
