
import pandas as pd
import numpy as np
import warnings
import plotly.express as px
import plotly.graph_objects as go

pd.options.display.float_format = '{:,.2f}'.format

selected_countries = [
    'Paraguai', 'Estados Unidos', 'China', 'Espanha', 'Haiti', 
    'Reino Unido', 'Paises Baixos', 'Japão', 'Alemanha', 'Uruguai'
            ]

def load_export_data():
    df = pd.read_excel('./ExportacaoVinhos.xlsx')
    df_inicial = df[df.columns[0:31]]
    df_melted = pd.melt(df_inicial, id_vars=['Pais'], var_name='Ano e Valor', value_name='Quantidade')
    df_melted[['Ano', 'Valor']] = df_melted['Ano e Valor'].str.split('_', expand=True)
    df_exportacao = df_melted.pivot(index=['Pais', 'Ano'], columns='Valor', values='Quantidade').reset_index()
    df_exportacao.columns.name = None 
    df_exportacao = df_exportacao.rename(columns={'KG': 'Litros', 'Pais' : 'Destino'})
    df_exportacao['Origem'] = 'Brasil'
    df_exportacao['Ano'] = pd.to_datetime(df_exportacao['Ano'], format='%Y')
    df_exportacao['Litros'] = df_exportacao['Litros'].astype(float)
    df_exportacao['USD'] = df_exportacao['USD'].astype(float)
    df_exportacao = df_exportacao[df_exportacao['Destino'].isin(selected_countries)]
    return df_exportacao


def load_country_sum(df_exportacao):
    df_total_por_pais = df_exportacao.groupby(['Origem','Destino']).sum(['Litros','USD']).sort_values('Litros', ascending=False)
    df_total_por_pais.reset_index(inplace=True)
    df_total_por_pais['USD_por_Litro'] = df_total_por_pais['USD'] / df_total_por_pais['Litros']
    return df_total_por_pais


def load_prod_exp():
    df_producao_exportacao = pd.read_excel('./ProducaoExportacao.xlsx')
    df_producao_exportacao['Ano'] = df_producao_exportacao['Ano'].astype('str')
    df_producao_exportacao['Produzido'] = df_producao_exportacao['Produzido'].astype(float)
    df_producao_exportacao['Exportado'] = df_producao_exportacao['Exportado'].astype(float)
    df_producao_exportacao['PTAX'] = df_producao_exportacao['PTAX'].astype(float)
    return df_producao_exportacao


def load_top10():
    df_top10 = pd.read_excel('./top10.xlsx')
    df_top10['Ano'] = pd.to_datetime(df_top10['Ano'], format='%Y')
    df_top10['Litros'] = df_top10['Litros'].astype(float)
    
    df_pivot = df_top10.pivot_table(index=['Ano', 'Pais'], columns='Variavel', values='Litros', aggfunc='sum').reset_index()
    df_pivot.fillna(0, inplace=True)
    df_pivot['Saldo'] =  df_pivot['Produção'] + df_pivot['Importação'] - df_pivot['Exportação'] - df_pivot['Consumo']

    return df_pivot
    

def load_economia():
    df_economia = pd.read_excel('./WEO_Data.xlsx')
    df_economia['Ano'] = pd.to_datetime(df_economia['Ano'], format='%Y')
    df_pivot_economia = df_economia.pivot_table(index=['Ano', 'Pais'], columns='Variavel', values='Percentual', aggfunc='sum').reset_index()
    df_pivot_economia.fillna(0, inplace=True)
    return df_pivot_economia