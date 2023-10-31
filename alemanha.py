import streamlit as st
import graficos_pais as gp
import brasil as br
import DataPreparation as dt


def load_total(df_pais, variavel):
    metrica = df_pais[variavel].sum()
    st.metric(label=f"{variavel} Total", value="{:,.0f}".format(metrica))

def load_saldo(df_pais):
    metrica = df_pais['Produção'].sum() + df_pais['Importação'].sum() - df_pais['Exportação'].sum() - df_pais['Consumo'].sum()
    st.metric(label=f"Saldo", value="{:,.0f}".format(metrica))

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