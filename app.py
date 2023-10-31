import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import begin as bg
import brasil as br
import country_pages as cp
import DataPreparation as dt
from pathlib import Path

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.options.display.float_format = '{:,.2f}'.format

st.set_page_config(
    page_title="Exportação de Vinhos Brasileiros",
    layout="wide",
    page_icon="🍷"
)

# custom_html = """
# <div class="banner">
#     <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
# </div>
# <style>
#     .banner {
#         width: 160%;
#         height: 200px;
#         overflow: hidden;
#     }
#     .banner img {
#         width: 100%;
#         object-fit: cover;
#     }
# </style>
# """
# # Display the custom HTML
# st.components.v1.html(custom_html)

# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)

st.markdown(f""" <style>
    .appview-container .main .block-container{{
        padding-top: {0}rem;
        padding-right: {1.5}rem;
        padding-left: {1.5}rem;
        padding-bottom: {0}rem;
    }} </style> """, unsafe_allow_html=True)

col1, col2 = st.columns(spec=[15,75], gap="medium")
with col1:
    st.image('https://raw.githubusercontent.com/alexandre-guerra/Exportacao/master/garrafa.jpg', use_column_width=True)
with col2:
    st.header(" ",divider='rainbow')
    st.title(":gray[Análise das Exportações de Vinhos Brasileiros 2008-2022]")

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
                                                                                                   'Bibliografia'],)


with begin:
    bg.Begin()    

with Brasil:
    br.load_country_page()

with Alemanha:
    cp.load_country_page('Alemanha')

with Paraguai:
    cp.load_country_page('Paraguai')

with EstadosUnidos:
    cp.load_country_page('Estados Unidos')

with China:
    cp.load_country_page('China')

with Espanha:
    cp.load_country_page('Espanha')

with Haiti:
    cp.load_country_page('Haiti')

with ReinoUnido:
    cp.load_country_page('Reino Unido')

with PaisesBaixos:
    cp.load_country_page('Paises Baixos')

with Japao:
    cp.load_country_page('Japão')

with Uruguai:
    cp.load_country_page('Uruguai')

with Conclusao:
    cp.conclusion()

with Bibliografia:
    cp.Bibliography()


    