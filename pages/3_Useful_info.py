import streamlit as st
from constants import VACANCY_TITLES

st.sidebar.page_link("streamlit_app.py", label="Главная")
st.sidebar.page_link("pages/1_Analytics.py", label="Анализ зарплат")
st.sidebar.page_link("pages/2_Salary_Prediction.py", label="Предсказание заработной платы")
st.sidebar.page_link("pages/3_Useful_info.py", label="Полезная информация")

st.title("Полезное")
st.subheader("Поисковые запросы")
st.text("Здесь вы можете скопировать готовые поисковые запросы по основным профессиям, чтобы значительно улучшить "
        "результаты поисковой выдачи на hh.ru")

for key, value in VACANCY_TITLES.items():
    st.text(key)
    st.code(value, language='text')
