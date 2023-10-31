import streamlit as st
import graficos_pais as gp


def load_total(df_pais, variavel):
    metrica = df_pais[variavel].sum()
    st.metric(label=f"{variavel} Total", value="{:,.0f}".format(metrica))

def load_saldo(df_pais):
    metrica = df_pais['Produção'].sum() + df_pais['Importação'].sum() - df_pais['Exportação'].sum() - df_pais['Consumo'].sum()
    st.metric(label=f"Saldo", value="{:,.0f}".format(metrica))

def conclusion():
    st.header("Conclusão")
    st.write(f"""
                O Brasil, reconhecido por sua rica diversidade vitivinícola, é um robusto produtor de vinhos. Contudo, curiosamente, apenas cerca de 2% desta produção é exportada, conforme indicado pelos registros da ApexBrasil. A boa notícia é que este cenário vem evoluindo positivamente. A cada ano, observamos um incremento tanto na quantidade quanto nos valores de vinhos exportados. Esta ascensão é, em grande parte, atribuída aos esforços e investimentos da ApexBrasil, especialmente por meio de seu projeto "Setorial Wines of Brazil", executado em colaboração com a União Brasileira de Vitivinicultura.

                Distribuídas de norte a sul do país, temos mais de 1.100 vinícolas, com a região Sul se destacando por contribuir com aproximadamente 90% da produção vinícola nacional.

                As estatísticas detalhadas sobre a produção e exportação dos vinhos brasileiros foram extraídas do site: vitibrasil.cnpuv.embrapa.br
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