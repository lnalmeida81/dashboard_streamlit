import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Site Streamlit")

with st.container():
    st.title("Dashboard com o Streamlit")
    st.subheader("Meu primeiro site com o Streamlit")
    st.write("Meu primeiro site com o Streamlit")
    st.write("Quer aprender Python? [Clique aqui](https://www.hashtagtreinamentos.com/curso-python)")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7 dias", "14 dias", "21 dias", "30 dias"])
    num_dias = int(qtde_dias.replace("dias", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")
