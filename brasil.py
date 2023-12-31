import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import DataPreparation as dt


ANNOTATIONS = [dict(
                x=1,
                y=-0.28,
                xref='paper',
                yref='paper',
                text='* Escala Logarítmica',
                showarrow=False,
                font=dict(size=12)
                )]

TITLE = dict(size=20)
STANDOFF = 30


def load_brasil(df_total_por_pais):
    st.dataframe(df_total_por_pais, hide_index=True, height=400, use_container_width=True)
    return df_total_por_pais


def load_total_litros_brasil(df_total_por_pais):    
    left, center, right = st.columns([1, 2, 1])
    with center:  
        st.subheader("$\sum$ Litros", divider='rainbow')
        st.header("{:,.0f}".format(df_total_por_pais['Litros'].sum()))
    

def load_total_usd_brasil(df_total_por_pais):
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.subheader("$\sum$ USD", divider='rainbow')
        st.header("{:,.0f}".format(df_total_por_pais['USD'].sum()))

def load_medio_usd_brasil(df_total_por_pais):
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.subheader("$\overline{USD}$ Por Litro", divider='rainbow')
        st.header("{:,.4f}".format(df_total_por_pais['USD_por_Litro'].mean()))


def load_prod_exp_brasil(df_producao_exportacao):
    st.dataframe(df_producao_exportacao, hide_index=True, height=400, use_container_width=True)
    return df_producao_exportacao


def load_total_prod_brasil(df_producao_exportacao):
    left, center, right = st.columns([1, 3, 1])
    with center:  
        total_produzido = df_producao_exportacao['Produzido'].sum()
        st.subheader("$\sum$ Produzido", divider='rainbow')
        st.header("{:,.0f}".format(total_produzido))


def load_total_exp_brasil(df_producao_exportacao):
    left, center, right = st.columns([1, 2, 1])
    with center:  
        total_exportado = df_producao_exportacao['Exportado'].sum()
        st.subheader("$\sum$ Exportado", divider='rainbow')
        st.header("{:,.0f}".format(total_exportado))


def load_total_percent_brasil(df_producao_exportacao):
    left, center, right = st.columns([1, 2, 1])
    with center:
        percentual_exportado = (df_producao_exportacao['Exportado'].sum()/df_producao_exportacao['Produzido'].sum()) * 100
        st.subheader("$\%$ Exportado", divider='rainbow')
        st.header("{:,.2f}%".format(percentual_exportado))


def load_graf_prod_exp_brasil(df_producao_exportacao):
    fig = px.bar(df_producao_exportacao.sort_values(by='Ano'), x='Ano', y=['Produzido','Exportado'], title='Produzido vs Exportado', barmode='group')

    fig.update_layout(
        title_font=TITLE, 
        xaxis_title='Anos',
        xaxis_title_standoff=STANDOFF,
        yaxis_title='Milhões de Litros',
        yaxis_type="log",
        yaxis_showticklabels=False,
        legend_title_text='',
        template="plotly_dark",
        annotations=ANNOTATIONS
    )

    fig.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)


def load_graf_variacao_prod_anual_brasil(df_producao_exportacao):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Produzido'], name='Produzido'))
    fig.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    fig.add_trace(go.Scatter(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Produzido'], mode='lines', name='Tendência'))

    fig.update_layout(title='Variação da Produção Anual com Linha de Tendência',
                    barmode='group',
                    title_font=TITLE, 
                    xaxis_title='Anos',
                    yaxis_type="log",
                    yaxis_showticklabels=False,
                    xaxis_title_standoff=STANDOFF,
                    showlegend=False, 
                    yaxis_title='Milhões de Litros',
                    template="plotly_dark",
                    annotations=ANNOTATIONS
                    )
    
    
    st.plotly_chart(fig, use_container_width=True)


def load_graf_variacao_exportacao_anual_brasil(df_producao_exportacao):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Exportado'], name='Exportado'))
    fig.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    fig.add_trace(go.Scatter(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Exportado'], mode='lines', name='Tendência'))
    fig.update_layout(title='Variação da Exportação Anual com Linha de Tendência',
                    barmode='group',
                    title_font=TITLE, 
                    xaxis_title='Anos',
                    yaxis_type="log",
                    xaxis_title_standoff=STANDOFF,
                    yaxis_showticklabels=False,
                    showlegend=False, 
                    yaxis_title='Milhões de Litros',
                    template="plotly_dark",
                    annotations=ANNOTATIONS
                    )
    
    st.plotly_chart(fig, use_container_width=True)


def load_graf_variacao_ptax_brasil(df_producao_exportacao):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['PTAX'], name='PTAX'))
    fig.update_traces(texttemplate='%{y:.4s}', textposition='outside', textfont_size=10)
    fig.add_trace(go.Scatter(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['PTAX'], mode='lines', name='Tendência'))
    fig.update_layout(title='Variação da PTAX Anual com Linha de Tendência',
                    yaxis_title='Reais (BRL)',
                    barmode='group',
                    title_font=TITLE, 
                    xaxis_title='Anos',
                    yaxis_type="log",
                    xaxis_title_standoff=STANDOFF,
                    yaxis_showticklabels=False,
                    showlegend=False,
                    template="plotly_dark",
                    annotations=ANNOTATIONS
                    )
    
    st.plotly_chart(fig, use_container_width=True)

def load_graf_vol_brasil(df_total_top10):
    fig = px.bar(df_total_top10, x='Destino', y=['Litros'], title='Distribuição em Volume por Destino')

    fig.update_layout(
        title_font=TITLE, 
        xaxis_title='Países',
        xaxis_title_standoff=STANDOFF,
        yaxis_title='Milhões de Litros',
        yaxis_type="log",
        yaxis_showticklabels=False,
        showlegend=False, 
        template="plotly_dark",
        annotations=ANNOTATIONS
    )

    fig.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)


def load_graf_usd_brasil(df_total_top10):
    fig = px.bar(df_total_top10.sort_values('USD', ascending=False), x='Destino', y=['USD'], title='Distribuição em Dólares por Destino')

    fig.update_layout(
        title_font=TITLE, 
        xaxis_title='Países',
        xaxis_title_standoff=STANDOFF,
        yaxis_title='Milhões de Dólares',
        yaxis_type="log",
        yaxis_showticklabels=False,
        showlegend=False, 
        template="plotly_dark",
        annotations=ANNOTATIONS
    )

    fig.update_traces(texttemplate='US$ %{y:.2s}', textposition='outside', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)


def load_graf_usd_litro_brasil(df_total_top10):
    fig = px.bar(df_total_top10.sort_values(by='USD_por_Litro',ascending=False), x='Destino', y=['USD_por_Litro'], title='Valor em Dolar por Litro no Destino')

    fig.update_layout(
        title_font=TITLE, 
        xaxis_title='Países',
        xaxis_title_standoff=STANDOFF,
        yaxis_title='Dólares',
        yaxis_type="log",
        yaxis_showticklabels=False,
        showlegend=False, 
        template="plotly_dark",
        annotations=ANNOTATIONS
    )

    fig.update_traces(texttemplate='US$ %{y:.2s}', textposition='outside', textfont_size=10)
    st.plotly_chart(fig, use_container_width=True)

def load_country_page():
    df_exportacao = dt.load_export_data()
    df_country_sum = dt.load_country_sum(df_exportacao)
    df_prod_exp = dt.load_prod_exp()

    st.text(" ")
    st.subheader("Brasil - Análise Total Exportado por Destino", divider='rainbow')
    st.text(" ")
    col1, col2 = st.columns(spec=[40,60], gap="large")
    with col1:
        load_brasil(df_country_sum)

    with col2:
        load_graf_vol_brasil(df_country_sum)        
    
    st.divider()
    col1, col2= st.columns(spec=2, gap="large")
    with col1:
        load_graf_usd_brasil(df_country_sum)

    with col2:
        load_graf_usd_litro_brasil(df_country_sum)
    

    st.divider()
    col1, col2, col3 = st.columns(spec=3, gap="large")
    with col1:
        load_total_litros_brasil(df_country_sum)

    with col2:
        load_total_usd_brasil(df_country_sum)

    with col3:
        load_medio_usd_brasil(df_country_sum)


    st.divider()
    st.subheader("Análise Anual de Produção, Exportação e Variação Cambial ", divider='rainbow')
    st.text(" ")
    col1, col2 = st.columns(spec=[40,60], gap="large")
    with col1:
        load_prod_exp_brasil(df_prod_exp)
    
    with col2:
        load_graf_variacao_prod_anual_brasil(df_prod_exp)
        

    st.divider()
    col1, col2 = st.columns(spec=2, gap="large")
    
    with col1:
        load_graf_variacao_exportacao_anual_brasil(df_prod_exp)

    with col2:
        load_graf_variacao_ptax_brasil(df_prod_exp)

    st.divider()
    load_graf_prod_exp_brasil(df_prod_exp)   
    st.divider()
    col1, col2, col3 = st.columns(spec=3, gap="large")
    with col1:
        load_total_prod_brasil(df_prod_exp)

    with col2:
        load_total_exp_brasil(df_prod_exp)

    with col3:
        load_total_percent_brasil(df_prod_exp)

    st.divider()