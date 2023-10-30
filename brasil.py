import streamlit as st
import DataPreparation as dt
import plotly.express as px
import pandas as pd

def load_brasil():
    df_exportacao = dt.load_export_data()
    df_total_por_pais = dt.load_country_sum(df_exportacao)
    st.header("Exportações Brasileiras de Vinhos")
    st.dataframe(df_total_por_pais, hide_index=True)
    return df_total_por_pais

def load_ptax_brasil():
    df_producao_exportacao = pd.read_excel('./ProducaoExportacao.xlsx')
    df_producao_exportacao['Ano'] = pd.to_datetime(df_producao_exportacao['Ano'], format='%Y')
    df_producao_exportacao['Ano'] = df_producao_exportacao['Ano'].dt.year.astype('Int64')
    df_producao_exportacao['Produzido'] = df_producao_exportacao['Produzido'].astype(float)
    df_producao_exportacao['Exportado'] = df_producao_exportacao['Exportado'].astype(float)
    df_producao_exportacao['PTAX'] = df_producao_exportacao['PTAX'].astype(float)
    st.header("Produção vs Exportação vs PTAX")
    st.dataframe(df_producao_exportacao, hide_index=True)

def load_graf_vol_brasil(df_total_top10):
    fig = px.bar(df_total_top10, x='Destino', y=['Litros'], title='Distribuição em Volume por Destino')

    fig.update_layout(
        title_font=dict(size=24), 
        xaxis_title='Países',
        xaxis_title_standoff=55,
        yaxis_title='Milhões de Litros',
        yaxis_type="log",
        yaxis_showticklabels=False,
        showlegend=False, 
        template="plotly_dark",
        annotations=[
            dict(
                x=1,
                y=-0.32,
                xref='paper',
                yref='paper',
                text='* Escala Logarítmica',
                showarrow=False,
                font=dict(size=12)
            )
        ]
    )

    fig.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)


def load_graf_usd_brasil(df_total_top10):
    fig = px.bar(df_total_top10.sort_values('USD', ascending=False), x='Destino', y=['USD'], title='Distribuição em Dólares por Destino')

    fig.update_layout(
        title_font=dict(size=24), 
        xaxis_title='Países',
        xaxis_title_standoff=55,
        yaxis_title='Milhões de Dólares',
        yaxis_type="log",
        yaxis_showticklabels=False,
        showlegend=False, 
        template="plotly_dark",
        annotations=[
            dict(
                x=1,
                y=-0.32,
                xref='paper',
                yref='paper',
                text='* Escala Logarítmica',
                showarrow=False,
                font=dict(size=12)
            )
        ]
    )

    fig.update_traces(texttemplate='US$ %{y:.2s}', textposition='outside', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)

def load_graf_usd_litro_brasil(df_total_top10):
    fig = px.bar(df_total_top10.sort_values(by='USD_por_Litro',ascending=False), x='Destino', y=['USD_por_Litro'], title='Valor em Dolar por Litro no Destino')

    fig.update_layout(
        title_font=dict(size=24), 
        xaxis_title='Países',
        xaxis_title_standoff=55,
        yaxis_title='Dólares',
        yaxis_type="log",
        yaxis_showticklabels=False,
        showlegend=False, 
        template="plotly_dark",
        annotations=[
            dict(
                x=1,
                y=-0.32,
                xref='paper',
                yref='paper',
                text='* Escala Logarítmica',
                showarrow=False,
                font=dict(size=12)
            )
        ]
    )

    fig.update_traces(texttemplate='US$ %{y:.2s}', textposition='outside', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)