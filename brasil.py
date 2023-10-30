import streamlit as st
import DataPreparation as dt

def load_brasil():
    df_exportacao = dt.load_export_data()
    df_total_por_pais = dt.load_country_sum(df_exportacao)
    st.header("Exportações Brasileiras de Vinhos")
    st.dataframe(df_total_por_pais, use_container_width=True)