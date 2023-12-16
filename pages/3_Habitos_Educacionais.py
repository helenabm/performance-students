import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    data = pd.read_csv('performance_students.csv')
    return data

data = load_data()

st.title('Dashboard Performance de Estudantes')

st.markdown("Análise de acordo com os hábitos educacionais dos estudantes.")

menu_options = ['Weekly study hours', 'Attendance to the seminars/conferences related to the department', 'Attendance to classes']
menu = st.sidebar.selectbox('Selecione uma opção:', ['Nenhuma'] + menu_options)

# Análise por horas semanais de estudo
if menu == 'Weekly study hours':
    st.header('Horas semanais de estudo dos Estudantes')
    data['Weekly study hours'] = data['Weekly study hours'].map({1: 'Nenhuma', 2: '<5 horas', 3: '6-10 horas', 4: '11-20 horas', 5: '+20 horas'})
    study_hours_counts = data['Weekly study hours'].value_counts().sort_index().reset_index()
    study_hours_counts.columns = ['Horas Semanais de Estudo', 'Contagem']
    fig_study_hours_counts_pie = px.pie(study_hours_counts, names='Horas Semanais de Estudo', values='Contagem', labels={'Classe': 'Classe', 'Contagem': 'Contagem'})
    st.plotly_chart(fig_study_hours_counts_pie)

# Desempenho dos estudantes por horas semanais de estudo
    st.subheader('Desempenho dos estudantes de acordo com as Horas de Estudos Semanais')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_study_hours_bar = px.histogram(data.dropna(), x='Weekly study hours', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desempenho'})
    fig_study_hours_bar.update_layout(yaxis_title='Contagem', xaxis_title='Horas Semanais de Estudo', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_study_hours_bar)

# Análise por resença nos seminários/conferências relacionados ao curso
elif menu == 'Attendance to the seminars/conferences related to the department':
    st.header('Presença nos seminários/conferências relacionados ao curso')
    data['Attendance to the seminars/conferences related to the department'] = data['Attendance to the seminars/conferences related to the department'].map({1: 'Sim', 2: 'Não'})
    seminars_conferences_counts = data['Attendance to the seminars/conferences related to the department'].value_counts().sort_index().reset_index()
    seminars_conferences_counts.columns = ['Presença em seminários/conferências relacionadas ao curso', 'Contagem']
    fig_seminars_conferences_counts_pie = px.pie(seminars_conferences_counts, names='Presença em seminários/conferências relacionadas ao curso', values='Contagem', labels={'Classe': 'Classe', 'Contagem': 'Contagem'})
    st.plotly_chart(fig_seminars_conferences_counts_pie)

    st.subheader('Desempenho dos estudantes de acordo com a presença nos seminários/conferências relacionados ao curso')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_seminars_conferences_counts_bar = px.histogram(data.dropna(), x='Attendance to the seminars/conferences related to the department', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desempenho'})
    fig_seminars_conferences_counts_bar.update_layout(yaxis_title='Contagem', xaxis_title='Presença em seminários/conferências relacionadas ao curso', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_seminars_conferences_counts_bar)

# Análise por atenção na aula
elif menu == 'Attendance to classes':
    st.header('Antenção nas aulas')
    data['Attendance to classes'] = data['Attendance to classes'].map({1: 'Sempre', 2: 'Ás vezes', 3: 'Nunca'})
    attendance_classes_counts = data['Attendance to classes'].value_counts().sort_index().reset_index()
    attendance_classes_counts.columns = ['Atenção nas aulas', 'Contagem']
    fig_attendance_classes_counts_pie = px.pie(attendance_classes_counts, names='Atenção nas aulas', values='Contagem', labels={'Antenção nas aulas': 'Antenção nas aulas', 'Contagem': 'Contagem'})
    st.plotly_chart(fig_attendance_classes_counts_pie)

    st.subheader('Desempenho de acordo com a Atenção nas Aulas')
    data['GRADE'] = data['GRADE'].map({0: 'Reprovado', 1: 'Desempenho excepcional', 2: 'Desempenho confortável', 3:'Cumprindo com competência', 4:'Cumprindo bem', 5:'Bom desempenho', 6:'Bom  desempenho e algumas excelências', 7:'Excelência absoluta'})
    fig_attendance_classes_bar = px.histogram(data.dropna(), x='Attendance to classes', color='GRADE', barmode='stack', nbins=20, labels={'x': 'Desempenho'})
    fig_attendance_classes_bar.update_layout(yaxis_title='Contagem', xaxis_title='Atenção nas aulas', legend_title='Desempenho do Estudante')
    st.plotly_chart(fig_attendance_classes_bar)

    

