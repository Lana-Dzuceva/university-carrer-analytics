import streamlit as st
from constants import VACANCY_TITLES


st.title("Полезное")
st.subheader("Поисковые запросы")
st.text("Здесь вы можете скопировать готовые поисковые запросы по основным профессиям, чтобы значительно улучшить "
        "результаты поисковой выдачи на hh.ru")

for key, value in VACANCY_TITLES.items():
    st.text(key)
    st.code(value, language='text')
