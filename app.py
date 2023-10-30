import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import begin as bg
import DataPreparation as dt

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.options.display.float_format = '{:,.2f}'.format


st.set_page_config(
    page_title="Exportação de Vinhos Brasileiros",
    layout="wide"
)



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
    df_exportacao = dt.load_export_data()
    df_total_por_pais = dt.load_country_sum(df_exportacao)
    st.header("Exportações Brasileiras de Vinhos")
    st.dataframe(df_total_por_pais, use_container_width=True)

