import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_excel('./ExportacaoVinhos.xlsx')
df_inicial = df[df.columns[0:31]]

df_melted = pd.melt(df_inicial, id_vars=[
                    'Pais'], var_name='Ano e Valor', value_name='Quantidade')
df_melted[['Ano', 'Valor']] = df_melted['Ano e Valor'].str.split(
    '_', expand=True)
df_exportacao = df_melted.pivot(
    index=['Pais', 'Ano'], columns='Valor', values='Quantidade').reset_index()
df_exportacao.columns.name = None
df_exportacao = df_exportacao.rename(
    columns={'KG': 'Litros', 'Pais': 'Destino'})
df_exportacao['Origem'] = 'Brasil'
df_exportacao['Ano'] = pd.to_datetime(df_exportacao['Ano'], format='%Y')
df_exportacao['Litros'] = df_exportacao['Litros'].astype(float)
df_exportacao['USD'] = df_exportacao['USD'].astype(float)

df_total_por_pais = df_exportacao.groupby(['Origem', 'Destino']).sum(
    ['Litros', 'USD']).sort_values('Litros', ascending=False)
df_total_por_pais.reset_index(inplace=True)
df_total_por_pais['USD_por_Litro'] = df_total_por_pais['USD'] / \
    df_total_por_pais['Litros']

top10 = df_total_por_pais.sort_values('Litros', ascending=False)[
    'Destino'].head(10).to_list()

df_total_top10 = df_total_por_pais[df_total_por_pais['Destino'].isin(top10)]
df_exportacao_top10 = df_exportacao[df_exportacao['Destino'].isin(top10)]

fig = px.bar(df_total_top10, x='Destino', y=[
             'Litros'], title='Litros exportados destino')

st.write('## Análise de Exportação de Vinhos Brasileiros')
st.dataframe(df_total_por_pais, use_container_width=True)
st.plotly_chart(fig, use_container_width=True)
