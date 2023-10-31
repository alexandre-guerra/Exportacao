import streamlit as st
import graficos_pais as gp
import brasil as br
import DataPreparation as dt


def load_total(df_pais, variavel):
    metrica = df_pais[variavel].sum()
    st.metric(label=f"{variavel} Total", value="{:,.0f}".format(metrica))


def load_country_page(pais):

    st.text(" ")
    st.subheader(f"Análise Anualizada - {pais}", divider=True)
    st.text(" ")

    (figs, df_pivot) = gp.load_grafs(pais)

    col1, col2 = st.columns(spec=[70,30], gap="large")
    with col1:
        st.plotly_chart(figs[0], use_container_width=True)

    with col2:
        st.plotly_chart(figs[3], use_container_width=True)

    st.divider()
    col1, col2 = st.columns(spec=2, gap="large")
    with col1:
        st.plotly_chart(figs[2], use_container_width=True)

    with col2:
        st.plotly_chart(figs[1], use_container_width=True)
    
    st.divider()
    df_prod_exp = dt.load_prod_exp()
    col1, col2, col3, col4 = st.columns(spec=4, gap="large")
    with col1:
        load_total(df_pivot, 'Produção')

    with col2:
        load_total(df_pivot, 'Exportação')

    with col3:
        load_total(df_pivot, 'Importação')

    with col4:
        load_total(df_pivot, 'Consumo')

    st.divider()