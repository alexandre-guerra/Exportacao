import streamlit as st

def Begin():
    st.header("Introdução")
    st.write(f"""
                O Brasil, reconhecido por sua rica diversidade vitivinícola, é um robusto produtor de vinhos. Contudo, curiosamente, apenas cerca de 2% desta produção é exportada, conforme indicado pelos registros da ApexBrasil. A boa notícia é que este cenário vem evoluindo positivamente. A cada ano, observamos um incremento tanto na quantidade quanto nos valores de vinhos exportados. Esta ascensão é, em grande parte, atribuída aos esforços e investimentos da ApexBrasil, especialmente por meio de seu projeto "Setorial Wines of Brazil", executado em colaboração com a União Brasileira de Vitivinicultura.

                Distribuídas de norte a sul do país, temos mais de 1.100 vinícolas, com a região Sul se destacando por contribuir com aproximadamente 90% da produção vinícola nacional.

                As estatísticas detalhadas sobre a produção e exportação dos vinhos brasileiros foram extraídas do site: vitibrasil.cnpuv.embrapa.br
                """)

    st.header("Critérios de Seleção de Dados")
    st.write(f"""
                Para garantir uma análise precisa e significativa, foram estabelecidos os seguintes critérios de exclusão:

                Países que importaram menos de 1.000 litros ao longo dos 15 anos em estudo.
                Países que realizaram apenas 1 ou 2 compras durante o período investigado, excluindo transações realizadas em 2021 e 2022 (categorizados como compradores eventuais).
                Exclusão de dados relacionados à Rússia devido a uma anomalia em 2009, atribuída a um acordo comercial específico. Além disso, as incertezas associadas ao conflito com a Ucrânia tornam arriscado contar com esta parceria no momento atual.
                """)

    st.header("Amostra Analisada")

    selected_countries = [
    'Paraguai', 'Estados Unidos', 'China', 'Espanha', 'Haiti', 
    'Reino Unido', 'Paises Baixos', 'Japão', 'Alemanha', 'Uruguai'
            ]

    st.write(f"""
    Optei por direcionar a análise para os top 10 países em volume de exportação, os quais, juntos, representam impressionantes 90,82% do total de nossos registros. Os países selecionados são:
    \n- """ + "\n- ".join(selected_countries) + """
    """)