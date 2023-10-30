import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def load_brasil(df_total_por_pais):
    st.subheader("Exportações Brasileiras de Vinhos")
    st.dataframe(df_total_por_pais, hide_index=True, use_container_width=True)
    return df_total_por_pais


def load_prod_exp_brasil(df_producao_exportacao):
    st.subheader("Produção vs Exportação vs PTAX")
    st.dataframe(df_producao_exportacao, hide_index=True, use_container_width=True)
    return df_producao_exportacao


def load_graf_prod_exp_brasil(df_producao_exportacao):
    fig = px.bar(df_producao_exportacao.sort_values(by='Ano'), x='Ano', y=['Produzido','Exportado'], title='Produzido vs Exportado', barmode='group')

    fig.update_layout(
        title_font=dict(size=24), 
        xaxis_title='Anos',
        xaxis_title_standoff=55,
        yaxis_title='Milhões de Litros',
        yaxis_type="log",
        yaxis_showticklabels=False,
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


def load_graf_variacao_prod_anual_brasil(df_producao_exportacao):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Produzido'], name='Produzido'))
    fig.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    fig.add_trace(go.Scatter(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Produzido'], mode='lines', name='Tendência'))

    fig.update_layout(title='Variação da Produção Anual com Linha de Tendência',
                    barmode='group',
                    title_font=dict(size=24), 
                    xaxis_title='Anos',
                    yaxis_type="log",
                    yaxis_showticklabels=False,
                    xaxis_title_standoff=55,
                    showlegend=False, 
                    yaxis_title='Produção em Milhões de Litros',
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
                        ])
    
    
    st.plotly_chart(fig, use_container_width=True)


def load_graf_variacao_exportacao_anual_brasil(df_producao_exportacao):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Exportado'], name='Exportado'))
    fig.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    fig.add_trace(go.Scatter(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['Exportado'], mode='lines', name='Tendência'))
    fig.update_layout(title='Variação da Exportação Anual com Linha de Tendência',
                    barmode='group',
                    title_font=dict(size=24), 
                    xaxis_title='Anos',
                    yaxis_type="log",
                    xaxis_title_standoff=55,
                    yaxis_showticklabels=False,
                    showlegend=False, 
                    yaxis_title='Exportação em Milhões de Litros',
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
                    ])
    
    st.plotly_chart(fig, use_container_width=True)


def load_graf_variacao_ptax_brasil(df_producao_exportacao):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['PTAX'], name='PTAX'))
    fig.update_traces(texttemplate='%{y:.4s}', textposition='outside', textfont_size=10)
    fig.add_trace(go.Scatter(x=df_producao_exportacao['Ano'], y=df_producao_exportacao['PTAX'], mode='lines', name='Tendência'))
    fig.update_layout(title='Variação da PTAX Anual com Linha de Tendência',
                    yaxis_title='PTAX',
                    barmode='group',
                    title_font=dict(size=24), 
                    xaxis_title='Anos',
                    yaxis_type="log",
                    xaxis_title_standoff=55,
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
                    ])
    
    st.plotly_chart(fig, use_container_width=True)

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