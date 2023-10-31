import plotly.express as px
import plotly.graph_objects as go
import DataPreparation as dt

ANNOTATIONS = [dict(
                x=1,
                y=-0.25,
                xref='paper',
                yref='paper',
                text='* Escala Logarítmica',
                showarrow=False,
                font=dict(size=12)
                )]

TITLE = dict(size=20)
STANDOFF = 30

def load_grafs(pais):
    figs = []

    df_exportacao = dt.load_export_data()
    df_pivot = dt.load_top10()
    df_economia = dt.load_economia()

    df_pais = df_pivot[df_pivot['Pais'] == pais]
    df_destino = df_exportacao[df_exportacao['Destino'] == pais]
    
    fig_destino = px.bar(df_destino, 
                x='Ano', 
                y='Litros', 
                title=f'Brasil para {pais} por ano',
                labels={'Litros': 'Litros Exportados', 'Ano': 'Ano'})
    
    fig_destino.update_layout(title=f'Importações do Brasil por Ano',
                    xaxis_title='Anos',
                    yaxis_title='Litros',
                    legend_title_text='',
                    yaxis_type="log",
                    xaxis_title_standoff=STANDOFF,
                    title_font=TITLE, 
                    template="plotly_dark",
                    showlegend=False, 
                    yaxis_showticklabels=False,
                    xaxis=dict(tickvals=df_pais['Ano'], ticktext=df_pais['Ano'].dt.year),
                    annotations=ANNOTATIONS)
    
    fig_destino.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)

    fig_dados = px.bar(df_pais,
                x="Ano",
                y=["Consumo", "Importação", "Produção", "Exportação"],
                barmode="group")
    
    fig_dados.update_layout(title=f'Comparativo de Dados Anuais',
                    xaxis_title='Anos',
                    yaxis_title='Litros',
                    legend_title_text='',
                    yaxis_type="log",
                    xaxis_title_standoff=STANDOFF,
                    title_font=TITLE, 
                    template="plotly_dark",
                    xaxis=dict(tickvals=df_pais['Ano'], ticktext=df_pais['Ano'].dt.year),
                    annotations=ANNOTATIONS)

    fig_saldo = go.Figure()
    fig_saldo.add_trace(go.Bar(x=df_pais['Ano'], y=df_pais['Saldo'], name='Saldo'))
    fig_saldo.update_traces(texttemplate='%{y:.2s}', textposition='outside', textfont_size=10)
    fig_saldo.add_trace(go.Scatter(x=df_pais['Ano'], y=df_pais['Saldo'], mode='lines', name='Tendência', line=dict(color='red')))
    
    fig_saldo.update_layout(title=f'Saldo Anual com Linha de Tendência',
                    xaxis_title='Anos',
                    yaxis_title='Litros',
                    legend_title_text='',
                    showlegend=False, 
                    title_font=TITLE,
                    xaxis_title_standoff=STANDOFF,
                    template="plotly_dark",
                    xaxis=dict(tickvals=df_pivot['Ano'], ticktext=df_pivot['Ano'].dt.year),
                    )
    
    
    
    fig_inflacao = go.Figure()
    subset = df_economia[df_economia['Pais'] == pais]
    fig_inflacao.add_trace(go.Scatter(x=subset['Ano'], y=subset['Inflação'],
                    mode='lines+markers',
                    name=pais))

    fig_inflacao.update_layout(title=f'Projeção de Inflação',
                    xaxis_title='Anos',
                    yaxis_title='Inflação (%)',
                    title_font=TITLE,
                    xaxis_title_standoff=STANDOFF,
                    template="plotly_dark",
                    xaxis=dict(tickvals=subset['Ano'], ticktext=subset['Ano'].dt.year))

    figs.append(fig_dados)
    figs.append(fig_saldo)
    figs.append(fig_destino)
    figs.append(fig_inflacao)
    return (figs, df_pais)

    # for fig in figs:
    #     st.plotly_chart(fig, use_container_width=True)


