import streamlit as st
import graficos_pais as gp


def load_total(df_pais, variavel):
    metrica = df_pais[variavel].sum()
    st.metric(label=f"{variavel} Total", value="{:,.0f}".format(metrica))

def load_saldo(df_pais):
    metrica = df_pais['Produção'].sum() + df_pais['Importação'].sum() - df_pais['Exportação'].sum() - df_pais['Consumo'].sum()
    st.metric(label=f"Saldo", value="{:,.0f}".format(metrica))

def conclusion():
    st.title("Análise de Viabilidade de Exportação de Vinhos")

    st.subheader("Dados e Análise - Estados Unidos")
    st.write("""
    Com base nos gráficos e dados fornecidos, aqui está uma análise preliminar:

    1. **Comparativo de Dados Anuais**: 
        - **Consumo**: O consumo tem sido bastante estável ao longo dos anos. 
        - **Produção**: A produção parece ter aumentado nos primeiros anos e depois se estabilizou.
        - **Exportação**: A exportação teve altos e baixos ao longo dos anos, mas nota-se uma queda acentuada em 2020 e 2022.

    2. **Importações do Brasil por Ano**: 
        - Houve uma diminuição geral nas importações ao longo dos anos, com algumas oscilações. A maior importação foi em 2008 com 440k e a menor em 2022 com 110k.

    3. **Projeção de Inflação**:
        - Espera-se que a inflação diminua nos próximos anos, o que pode favorecer o poder de compra dos consumidores.

    4. **Saldo Anual com Linha de Tendência**:
        - O saldo foi negativo na maioria dos anos, o que indica que o valor das importações superou o das exportações. No entanto, o saldo está melhorando ao longo dos anos, indicando uma tendência positiva.

    5. **Dados Adicionais**:
        - **Consumo Total**: 46,494,800,000
        - **Importação Total**: 16,918,300,000
        - **Produção Total**: 34,792,400,000
        - **Exportação Total**: 5,713,200,000
        - **Saldo**: -497,300,000

    Conclusão:
    O mercado brasileiro de vinhos apresenta um consumo estável e uma produção considerável. No entanto, as exportações são relativamente baixas em comparação com a produção, e o saldo é negativo, indicando que as importações superam as exportações.

    Ao considerar a exportação de vinhos para os EUA, é importante avaliar:
    - A qualidade e diferenciação dos vinhos brasileiros em relação aos vinhos já disponíveis nos EUA.
    - Os custos de exportação e as tarifas de importação nos EUA.
    - O potencial de marketing e a aceitação dos consumidores americanos.

    Dada a projeção de diminuição da inflação, pode haver uma oportunidade de aumentar a competitividade no mercado americano, mas é essencial considerar todos os fatores mencionados acima antes de tomar uma decisão.
    """)


def Bibliography():
    st.header("Bibliografia")

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


def load_country_page(pais):

    st.text(" ")
    st.subheader(f"{pais} - Análise Anualizada", divider=True)
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
        load_total(df_pivot, 'Consumo')
        load_total(df_pivot, 'Importação')
        load_total(df_pivot, 'Produção')
        load_total(df_pivot, 'Exportação')
        load_saldo(df_pivot)
        
        
    st.divider()