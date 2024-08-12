import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao


acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "GGBR4.SA"]
dados = carregar_dados(acoes)


st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.
         """)


st.sidebar.header("Filtros")


lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar",dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})     


data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()

intervalo_datas = st.sidebar.slider("Selecione o perído", min_value=data_inicial, max_value=data_final, 
                                    value=(data_inicial, data_final),
                                    step=timedelta(days=1))


dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]


st.line_chart(dados)

