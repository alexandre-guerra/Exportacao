import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import begin as bg
import brasil as br
import DataPreparation as dt

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.options.display.float_format = '{:,.2f}'.format


st.set_page_config(
    page_title="Exportação de Vinhos Brasileiros",
    layout="wide"
)

df_exportacao = dt.load_export_data()
df_country_sum = dt.load_country_sum(df_exportacao)
df_prod_exp = dt.load_prod_exp()

st.title("Análise das Exportações de Vinhos Brasileiros (2008-2022)")

# Navegação

begin, Brasil, Paraguai, EstadosUnidos, China, Espanha, Haiti, ReinoUnido, PaisesBaixos, Japao, Alemanha, Uruguai, Conclusao, Bibliografia = st.tabs(['Início',
                                                                                                   'Brasil',
                                                                                                   'Paraguai',
                                                                                                   'Estados Unidos',
                                                                                                   'China',
                                                                                                   'Espanha',
                                                                                                   'Haiti',
                                                                                                   'Reino Unido',
                                                                                                   'Paises Baixos',
                                                                                                   'Japão',
                                                                                                   'Alemanha',
                                                                                                   'Uruguai',
                                                                                                   'Conclusão',
                                                                                                   'Bibliografia'])





with begin:
    bg.Begin()    

with Brasil:
    col1, col2= st.columns(spec=[30,70])
    with col1:
        br.load_brasil(df_prod_exp)

    with col2:
        br.load_graf_vol_brasil(df_country_sum)

    col1, col2= st.columns(spec=2)
    with col1:
        br.load_graf_usd_brasil(df_country_sum)

    with col2:
        br.load_graf_usd_litro_brasil(df_country_sum)
    
    col1, col2= st.columns(spec=[30,70])
    with col1:
        br.load_prod_exp_brasil(df_prod_exp)
    
    with col2:
        br.load_graf_prod_exp_brasil(df_prod_exp)
    
    col1, col2, col3 = st.columns(spec=3)
    with col1:
        br.load_graf_variacao_prod_anual_brasil(df_prod_exp)

    with col2:
        br.load_graf_variacao_exportacao_anual_brasil(df_prod_exp)

    with col3:
        br.load_graf_variacao_ptax_brasil(df_prod_exp)

