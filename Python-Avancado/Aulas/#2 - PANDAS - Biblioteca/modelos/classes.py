import pandas as pd

class Dados:
    def __init__(self, dados):
        self._dados = pd.read_csv(dados, sep= ';')

    @property
    def dados(self):
        return self._dados

    def ler_inicio(self, linhas):
        return self._dados.head(linhas)

    def ler_final(self, linhas):
        return self._dados.tail(linhas)

    def ler_tipo(self):
        return type(self._dados)

    def ler_colunas(self):
        return self.dados.columns

    def tipo_dado_cabecalho(self, cabecalho):
        return self.dados[cabecalho]

    def media_rendas(self, agrupador, valor_de_media):
        return self._dados.groupby(agrupador)[valor_de_media].mean().round(2)

    def percentagem_tipo(self):
        return self._dados.Tipo.value_counts(normalize=True)

    def mostrar_valores_nulos(self):
        return self._dados.isnull().sum()

    def remover_valores_nulos(self, novo_valor):
        return self._dados.fillna(novo_valor, inplace=True)

    def encontrar_valores_zero(self):
        return self.dados.query('Quartos == 0 | Valor == 0 | Area == 0 | Condominio == 0')
    
    def remover_valores_zero(self):
        registo_a_remover = self.dados.query('Quartos == 0 | Valor == 0 | Area == 0 | Condominio == 0').index
        return self.dados.drop(registo_a_remover, axis = 0, inplace=True) 
    #axis (referencia para indice e colunas)
    
    def filtro_quarto(self, num_quartos):
        return self.dados['Quartos'] == num_quartos

    def filtro_aluguer(self, valor_aluguer):
        return self.dados['Valor'] < valor_aluguer
    
    def filtro_quarto_aluguer(self):
        filtro1 = self.dados['Quartos'] == 1
        filtro2 = self.dados['Valor'] < 500

        filtro_composto =  filtro1 & filtro2

        return  self.dados[filtro_composto]
    

    """ Apartamentos que tenham pelo menos 2 quartos, aluguer inferior a 750€ e uma área maior que 70 m². """

    def filtro_aluguel_tamanho(self):
        f1 = self.dados['Quartos'] == 2
        f2 = self.dados['Valor'] < 750
        f3 = self.dados['Area'] > 70

        os_tres = f1 & f2 & f3

        return self.dados[os_tres]
    
    def media_para_guardar(self):
        return self.dados.groupby('Tipo')['Valor'].mean().round(2)
    
    def guardar(self, nome_arquivo, metodo = None, separador = ';'):
        #UTF-8-sig permite acento das palavras SIG - força a utilizacao
        #Separador sep= ';'
        #decidir o que guardar
        if metodo: #metodo == True:
            df_para_guardar = metodo()
        else:
            df_para_guardar = self.dados

        #guardar o que foi decidido acima
        df_para_guardar.to_csv(nome_arquivo, index=False, sep=separador, encoding='UTF-8-sig')
        #Tem que especificar o nome do arquivo.
        print(f'{nome_arquivo}Arquivo Criado com sucesso!')

    def despesas_mensais(self):
        self.dados['Despesas Mensais'] = self.dados['Valor'] + self.dados['Condominio']
        return self.dados
    
    def despesas_anuais(self):
        self.dados['Despesas Anuais'] = self.dados['Valor'] + self.dados['Condominio'] * 12
        return self.dados