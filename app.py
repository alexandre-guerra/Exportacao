import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import begin as bg
import brasil as br

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
    df = br.load_brasil()
    br.load_graf_vol_brasil(df)
    br.load_graf_usd_brasil(df)

