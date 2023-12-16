import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('performance_students.csv')
    return data

data = load_data()

# Título do Dashboard
st.title('Dashboard Performance de Estudantes')
st.markdown("A base de dados usada nessa aplicação foi criada com o objetivo de avaliar o desempenho dos Estudantes na graduação. A base possui 33 colunas e 145 linhas. As colunas de 1 a 10 possuem dados pessoais do Estudante, as colunas de 11 a 16 são dados dos familiares e as colunas restantes incluem hábitos educacionais.")
st.subheader('Visão Geral da Base')
st.write(data.head())
st.markdown("Para mais informações sobre a base de dados basta acessar o link: https://www.kaggle.com/datasets/joebeachcapital/students-performance.")

#Correlação
st.subheader('Correlação do Desempenho do Estudante')

df_excluida = data.drop(columns=['STUDENT ID'])
correlation_matrix = df_excluida.corr()
coluna_escolhida = st.selectbox('Escolha uma coluna para calcular a correlação:', correlation_matrix.columns)
correlacao = correlation_matrix[coluna_escolhida].corr(correlation_matrix['GRADE'])
fig = px.scatter(correlation_matrix, x=coluna_escolhida, y='GRADE', trendline="ols", title=f'Correlação entre {coluna_escolhida} e Desempenho do Estudante')
st.plotly_chart(fig)
