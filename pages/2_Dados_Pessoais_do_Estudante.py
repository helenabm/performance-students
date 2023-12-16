import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    data = pd.read_csv('performance_students.csv')
    return data

data = load_data()

st.title('Dashboard Performance de Estudantes')

st.markdown("Análise de acordo com os dados pessoais dos estudantes.")

# Sidebar com opções
menu = st.sidebar.selectbox('Selecione uma opção:', ['Nenhuma'] + list(data.columns[1:7]))

#Correlação entre a coluna de desempenho e as outras colunas
if menu == 'Student Age':

    st.subheader('Distribuição dos estudantes por Idade')
    data['Student Age'] = data['Student Age'].map({1: '18-21 anos', 2: '22-25 anos', 3:'Acima de 26 anos'})
    age_type = data['Student Age'].value_counts().sort_index().reset_index()
    age_type.columns = ['Idade', 'Contagem']
    age_type_bar = px.bar(age_type, x='Idade', y='Contagem', labels={'Idade': 'Idade', 'Contagem': 'Contagem'})
    st.plotly_chart(age_type_bar)

    st.subheader('Desempenho dos estudantes por Idade')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_age_type = px.histogram(data.dropna(), x='Student Age', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desemepenho'})
    fig_age_type.update_layout(yaxis_title='Contagem', xaxis_title='Idade', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_age_type)

# Análise por sexo
elif menu == 'Sex':

    st.subheader('Distribuição dos estudantes por Sexo')
    data['Sex'] = data['Sex'].map({1: 'Feminino', 2: 'Masculino'})
    sex_type = data['Sex'].value_counts().sort_index().reset_index()
    sex_type.columns = ['Sex', 'Contagem']
    sex_type_bar = px.bar(sex_type, x='Sex', y='Contagem', labels={'Sexo': 'Sexo', 'Contagem': 'Contagem'})
    st.plotly_chart(sex_type_bar)

    st.subheader('Desempenho dos estudantes por Sexo')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_sex_type = px.histogram(data.dropna(), x='Sex', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desemepenho'})
    fig_sex_type.update_layout(yaxis_title='Contagem', xaxis_title='Sexo', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_sex_type)

# Análise por tipo de ensino médio
elif menu == 'Graduated high-school type':

    st.subheader('Distribuição dos estudantes por tipo de Ensino Médio')
    data['Graduated high-school type'] = data['Graduated high-school type'].map({1: 'Particular', 2: 'Estadual', 3:'Outro'})
    high_school_type = data['Graduated high-school type'].value_counts().sort_index().reset_index()
    high_school_type.columns = ['Tipo de ensino médio', 'Contagem']
    high_school_type_bar = px.bar(high_school_type, x='Tipo de ensino médio', y='Contagem', labels={'Tipo de ensino médio': 'Tipo de ensino médio', 'Contagem': 'Contagem'})
    st.plotly_chart(high_school_type_bar)

    st.subheader('Desempenho dos estudantes por tipo de Ensino Médio')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_high_school_type = px.histogram(data.dropna(), x='Graduated high-school type', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desemepenho'})
    fig_high_school_type.update_layout(yaxis_title='Contagem', xaxis_title='Tipo de Ensino Médio', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_high_school_type)

#Análise por tipo de bolsa
elif menu == 'Scholarship type':

    st.subheader('Distribuição dos estudantes por tipo de Bolsa')
    data['Scholarship type'] = data['Scholarship type'].map({1: 'Nenhuma', 2: 'Vinte e Cinco por cento', 3: 'Cinquenta por cento', 4: 'Setenta e Cinco por cento', 5: 'Integral'})
    scholarship_type = data['Scholarship type'].value_counts().sort_index().reset_index()
    scholarship_type.columns = ['Tipo de Bolsa', 'Contagem']
    scholarship_type_bar = px.bar(scholarship_type, x='Tipo de Bolsa', y='Contagem', labels={'Tipo de Bolsa': 'Tipo de Bolsa', 'Contagem': 'Contagem'})
    st.plotly_chart(scholarship_type_bar)

    st.subheader('Desempenho dos estudantes por tipo de Bolsa')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_scholarship_type = px.histogram(data.dropna(), x='Scholarship type', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desemepenho'})
    fig_scholarship_type.update_layout(yaxis_title='Contagem', xaxis_title='Tipo de Bolsa', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_scholarship_type)

# Análise por trabalho adicional
elif menu == 'Additional work':

    st.subheader('Distribuição dos estudantes por Trabalho Adicional')
    data['Additional work'] = data['Additional work'].map({1: 'Sim', 2: 'Não'})
    additional_work_type = data['Additional work'].value_counts().sort_index().reset_index()
    additional_work_type.columns = ['Trabalho Adicional', 'Contagem']
    additional_work_type_bar = px.bar(additional_work_type, x='Trabalho Adicional', y='Contagem', labels={'Trabalho Adicional': 'Trabalho Adicional', 'Contagem': 'Contagem'})
    st.plotly_chart(additional_work_type_bar)

    st.subheader('Desempenho dos estudantes por Trabalho Adicional')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_additional_work_type = px.histogram(data.dropna(), x='Additional work', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desemepenho'})
    fig_additional_work_type.update_layout(yaxis_title='Contagem', xaxis_title='Trabalho Adicional', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_additional_work_type)

# Análise por atividade esportiva ou artistica
elif menu == 'Regular artistic or sports activity':

    st.subheader('Distribuição dos estudantes por Atividade Esportiva ou Artística')
    data['Regular artistic or sports activity'] = data['Regular artistic or sports activity'].map({1: 'Sim', 2: 'Não'})
    sports_activity_type = data['Regular artistic or sports activity'].value_counts().sort_index().reset_index()
    sports_activity_type.columns = ['Possui Atividade Esportiva ou Artística', 'Contagem']
    sports_activity_type_bar = px.bar(sports_activity_type, x='Possui Atividade Esportiva ou Artística', y='Contagem', labels={'Tipo de Bolsa': 'Tipo de Bolsa', 'Contagem': 'Contagem'})
    st.plotly_chart(sports_activity_type_bar)

    st.subheader('Desempenho dos estudantes por Atividade Esportiva ou Artística')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_sports_activity_type = px.histogram(data.dropna(), x='Regular artistic or sports activity', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desemepenho'})
    fig_sports_activity_type.update_layout(yaxis_title='Contagem', xaxis_title='Possui Atividade Esportiva ou Artística', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_sports_activity_type)
