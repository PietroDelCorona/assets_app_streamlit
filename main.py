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

@st.cache_data
def carregar_ticker_acoes():
    base_tickers = pd.read_csv("IBOV.csv", sep=";")
    tickers = list(base_tickers["Código"])
    tickers = [item + ".SA" for item in tickers]
    return tickers


acoes = carregar_ticker_acoes()
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
    else:
        dados = dados[lista_acoes]     


data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()

intervalo_datas = st.sidebar.slider("Selecione o perído", min_value=data_inicial, max_value=data_final, 
                                    value=(data_inicial, data_final),
                                    step=timedelta(days=1))


dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]


st.line_chart(dados)


texto_performance_ativos = ""

if len(lista_acoes)==0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes)==1:
    dados = dados.rename(columns={"Close": acao_unica})

carteira = [1000 for acao in lista_acoes]
total_inicial_carteira = sum(carteira)

for i, acao in enumerate(lista_acoes):
    performance_ativos = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    performance_ativos = float(performance_ativos)

    carteira[i] = carteira[i] * (1 + performance_ativos)

    if performance_ativos > 0:
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :green[{performance_ativos:.1%}]"
    elif performance_ativos < 0:
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :red[{performance_ativos:.1%}]"
    else:
        texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: Dados não encontrados"

total_final_carteira = sum(carteira)
performance_carteira = total_final_carteira / total_inicial_carteira - 1

if performance_ativos > 0:
        texto_performance_carteira = f"Performance da carteira em todos os ativos: :green[{performance_carteira:.1%}]"
elif performance_ativos < 0:
    texto_performance_carteira =  f"Performance da carteira em todos os ativos: :red[{performance_carteira:.1%}]"
else:
    texto_performance_carteira = f"Performance da carteira em todos os ativos: Dados não encontrados"

st.write(f"""
### Performance dos Ativos
Essa foi a performance de cada ativo no período selecionado:
         
{texto_performance_ativos}

{texto_performance_carteira}
""")


