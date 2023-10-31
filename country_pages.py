import streamlit as st
import graficos_pais as gp


def load_total(df_pais, variavel):
    metrica = df_pais[variavel].sum()
    st.subheader(f"{variavel} Total", divider=True)
    st.header("{:,.0f}".format(metrica))

def load_saldo(df_pais):
    metrica = df_pais['Produção'].sum() + df_pais['Importação'].sum() - df_pais['Exportação'].sum() - df_pais['Consumo'].sum()
    st.subheader(f"Saldo Total", divider=True)
    st.header("{:,.0f}".format(metrica))

def conclusion():

    st.text(" ")
    st.subheader("Análise de Viabilidade de Exportação de Vinhos Brasileiros", divider=True)
    st.text(" ")
    st.markdown(f"""  
    ##### Produção
    A produção de vinhos teve uma queda significativa em 2016, a safra de uvas teve uma das maiores quebras registradas, com uma redução de 57% em relação ao ano anterior, equivalente, aproximadamente, a 300 milhões de quilos de uvas no território gaúcho. A principal causa da quebra histórica no ano 2016 foi uma série de acontecimentos climáticos que prejudicaram o desenvolvimento das uvas ao longo do ano, como geadas e excesso de chuvas, mas mostrou uma recuperação nos anos seguintes, especialmente entre 2017 e 2022.
    
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Exportação
    A quantidade de vinhos exportados apresentou variações ao longo dos anos. Em 2022, a quantidade de vinho exportado foi de 7.025.983 de litros, um número inferior ao pico recente de 8.058.704 de litros em 2021, mas ainda superior ao de muitos anos anteriores.
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Taxa de câmbio (PTAX)
    A taxa PTAX aumentou consistentemente desde 2008 até 2021, indicando uma desvalorização da moeda local frente ao dólar. Isso pode tornar as exportações mais atrativas, pois os produtos nacionais ficam mais competitivos em termos de preço. Em 2022, houve uma pequena retração nessa taxa.
    """)
    st.text(" ")
    st.markdown(f"""  
    #### Conclusão
    Considerando a recuperação na produção e a taxa de câmbio ainda elevada (apesar da pequena retração em 2022), pode ser um momento viável para entrar no mercado de exportação de vinhos. A desvalorização da moeda local pode ajudar a tornar os vinhos brasileiros mais competitivos em termos de preço no mercado internacional.
    """)

    st.divider()
    st.text(" ")
    st.subheader("Prospecções futuras e possíveis ações para uma melhoria", divider=True)
    st.text(" ")


    st.markdown("""  
    ##### USD por Litro
    Países como Reino Unido e Países Baixos têm um valor de USD por litro mais alto, indicando que eles podem valorizar vinhos de qualidade superior ou que há espaço para aumentar os preços nesses mercados.
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Principais Destinos
    Paraguai é o maior importador em termos de volume, mas o preço por litro é mais baixo. Países como Estados Unidos e Reino Unido importam menos em volume, mas o valor em USD é mais alto.
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Segmentação de Mercado
    Para mercados que pagam mais por litro, como Reino Unido e Países Baixos, pode-se focar em vinhos premium ou de edição limitada.
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Promoções e Degustações
    Em países com grande volume mas valor menor por litro, como o Paraguai, poderiam ser organizadas promoções e degustações para aumentar a percepção de valor do vinho brasileiro.
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Parcerias
    Estabelecer parcerias com distribuidores locais ou participar de feiras internacionais de vinho pode ajudar a aumentar a visibilidade e aceitação dos vinhos brasileiros nesses mercados.
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Branding e Marketing
    Investir em branding para posicionar o vinho brasileiro como uma escolha de qualidade e valor, destacando características únicas e diferenciais em relação a outros vinhos no mercado.
    """)
    st.text(" ")
    st.markdown(f"""  
    ##### Certificações
    Obter certificações de qualidade ou sustentabilidade pode aumentar a confiança e aceitação nos mercados internacionais.
                    """)
    
    st.divider()


def Bibliography():
    st.text(" ")
    st.subheader("Bibliografia", divider=True)
    st.text(" ")

    st.write("""
    Embrapa Uva e Vinho. (10/10/2023). Vitibrasil. http://vitibrasil.cnpuv.embrapa.br

    Agência Brasileira de Promoção de Exportações e Investimentos (Apex-Brasil). (21/10/2023). Página inicial. https://www.apexbrasil.com.br

    União Brasileira de Vitivinicultura (UBV). (21/10/2023). Página inicial. https://www.ubv.com.br

    Wines of Brasil. (21/10/2023). Página inicial. https://www.winesofbrasil.com

    Organização Mundial do Comércio (WTO). (27/10/2023). Página inicial. https://www.wto.org

    Banco Central do Brasil (BCB). (27/10/2023). Página inicial. https://www.bcb.gov.br

    Fundo Monetário Internacional (IMF). (29/10/2023). Página inicial. https://www.imf.org

    Ministério da Agricultura, Pecuária e Abastecimento (MAPA). (20/10/2023). Sistemas Web. https://sistemasweb.agricultura.gov.br

    Ministério da Agricultura, Pecuária e Abastecimento (MAPA). (20/10/2023). Estatísticas de comércio exterior. https://www.gov.br/agricultura/pt-br/assuntos/relacoes-internacionais/estatisticas-de-comercio-exterior

    Ministério da Agricultura, Pecuária e Abastecimento (MAPA). (20/10/2023). Dados abertos. https://dados.agricultura.gov.br/organization/mapa

    Organização Internacional da Vinha e do Vinho (OIV). (15/10/2023). Estatísticas. https://www.oiv.int/what-we-do/statistics
    """)
    st.divider()

def load_country_page(pais):

    st.text(" ")
    st.subheader(f":blue[{pais}] - Análise Anualizada", divider=True)
    st.text(" ")

    (figs, df_pivot) = gp.load_grafs(pais)

    st.plotly_chart(figs[0], use_container_width=True)

    st.divider()
    col1, col2 = st.columns(spec=[70,30], gap="large")
    with col1:
        st.plotly_chart(figs[2], use_container_width=True)

    with col2:
        st.plotly_chart(figs[3], use_container_width=True)
    

    st.divider()
    
    col1, col2 = st.columns(spec=[75,25], gap="large")

    with col1:
        st.plotly_chart(figs[1], use_container_width=True)

    with col2:
        st.header(" ")
        load_total(df_pivot, 'Consumo')
        st.header(" ")
        load_total(df_pivot, 'Importação')
    
    st.divider()

    col1, col2, col3 = st.columns(spec=3, gap="large")
    with col1:
        load_total(df_pivot, 'Produção')
    
    with col2:
        load_total(df_pivot, 'Exportação')
    
    with col3:
        load_saldo(df_pivot)


    st.divider()