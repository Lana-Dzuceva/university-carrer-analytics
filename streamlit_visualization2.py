# import streamlit as st
# import joblib
# import pandas as pd
# import time
#
#
# # Функция-заглушка для парсинга (замените на ваш метод)
# def parse_vacancy(url):
#     """
#     Принимает URL вакансии и возвращает данные для модели.
#     Замените на ваш реальный метод парсинга.
#     """
#     # Пример возвращаемых данных
#     return {
#         "name": "Python Developer",
#         "description": "Python developer with 3 years of experience in web development",
#     }
#
#
# # Функция для подготовки признаков (настройте под вашу модель)
# def prepare_features(data):
#     """
#     Преобразует данные в формат, подходящий для модели.
#     Замените на ваш код обработки (например, TF-IDF).
#     """
#     # Пример: возвращаем текстовое описание
#     # Если нужен TfidfVectorizer, раскомментируйте и настройте:
#     # vectorizer = joblib.load("tfidf_vectorizer.pkl")
#     # features = vectorizer.transform([data["description"]])
#     return [data["description"]]
#
#
# # Загрузка модели
# model = joblib.load("models/random_forest_model2.pkl")
#
# # Кастомный CSS для стилизации
# st.markdown("""
# <style>
#     .header {
#         background-color: #1f77b4;
#         padding: 1rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#         font-size: 2rem;
#         font-weight: bold;
#         margin-bottom: 2rem;
#     }
#     .footer {
#         background-color: #f0f2f6;
#         padding: 1rem;
#         border-radius: 10px;
#         text-align: center;
#         font-size: 0.9rem;
#         color: #333333;
#         margin-top: 2rem;
#     }
#     .stTextInput> div> div> input {
#         border: 2px solid #1f77b4;
#         border-radius: 5px;
#         padding: 0.5rem;
#     }
#     .stTextInput> div> div> input:disabled {
#         background-color: #f0f2f6;
#         color: #333333;
#     }
#     .vacancy-box {
#         background-color: #ffffff;
#         padding: 1rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         margin-bottom: 1rem;
#     }
# </style>
# """, unsafe_allow_html=True)
#
# tab1, tab2 = st.tabs(["Analytics", "Model"])
# with tab1:
#     st.text("Туть аналитика")
# with tab2:
#     # Хедер
#     st.markdown('<div class="header">Salary Prediction Dashboard</div>', unsafe_allow_html=True)
#
#     # Текстовое поле для ввода URL
#     st.subheader("Enter Vacancy URL")
#     url = st.text_input("URL", placeholder="https://example.com/vacancy/123", label_visibility="collapsed")
#
#     # Обработка URL и предсказание
#     if url:
#         with st.spinner("Processing vacancy..."):
#             try:
#                 # Парсинг данных
#                 vacancy_data = parse_vacancy(url)
#
#                 # Подготовка признаков
#                 features = prepare_features(vacancy_data)
#
#                 # Имитация задержки для демонстрации прогресс-бара
#                 time.sleep(1)
#
#                 # Предсказание зарплаты
#                 predicted_salary = model.predict(features)[0]  # Ожидается [salary_from, salary_to]
#                 salary_from, salary_to = predicted_salary
#
#                 # Вывод результатов
#                 st.subheader("Vacancy Details")
#                 st.markdown(f"""
#                 <div class="vacancy-box">
#                     <strong>Name:</strong> {vacancy_data['name']}<br>
#                     <strong>Description:</strong> {vacancy_data['description']}<br>
#                     <strong>Predicted Salary Range (RUB):</strong> {salary_from:,.0f} - {salary_to:,.0f}
#                 </div>
#                 """, unsafe_allow_html=True)
#
#             except Exception as e:
#                 st.error(f"Error processing the URL: {str(e)}")
#     else:
#         st.markdown("""
#         <div class="vacancy-box">
#             <strong>Name:</strong> Enter a URL to see the vacancy details<br>
#             <strong>Description:</strong> Waiting for input...<br>
#             <strong>Predicted Salary Range (RUB):</strong> Waiting for input...
#         </div>
#         """, unsafe_allow_html=True)
#
# # Футер
# st.markdown("""
# <div class="footer">
#     Powered by xAI | Built with Streamlit | Data processed with DuckDB and Random Forest
# </div>
# """, unsafe_allow_html=True)


import streamlit as st
import joblib
import pandas as pd
# import time
from prep_data_for_model import *


# Список доступных моделей
models = {
    "Случайный лес (v2)": "models/random_forest_model2.pkl",
    "Случайный лес (v1)": "models/random_forest_model2.pkl"  # Замените на реальные имена файлов
}

# Кастомный CSS для стилизации
st.markdown("""
<style>
    .header {
        background-color: #E57373;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .footer {
        background-color: rgba(0, 0, 0, 0.1);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 0.9rem;
        color: #4A4A4A;
        bottom: 0;
        width: 100%;
        left: 0;
    }
    .footer a {
        color: #E57373;
        text-decoration: none;
        margin: 0 0.5rem;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .stTextInput> div> div> input {
        border: 1px solid ;
        border-radius: 5px;
        padding: 0.5rem;
        color: #4A4A4A;
    }
    .stTextInput> div> div> input:disabled {
        background-color: #F5F5DC;
        color: #4A4A4A;
    }
    .vacancy-box {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        color: #4A4A4A;
    }
    .stApp {
        background-color: rgba(0, 0, 0, 0.02);
        min-height: 90vh;
        display: flex;
        flex-direction: column;
    }
    .main-content {
        flex: 1;
        padding-bottom: 4rem; /* Отступ для футера */
    }
</style>
""", unsafe_allow_html=True)
# background - color:  # F5F5DC;

# Хедер
st.markdown('<div class="header">Дашборд предсказания зарплаты</div>', unsafe_allow_html=True)

# Основной контент
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Выпадающий список для выбора модели
st.subheader("Выберите модель")
selected_model = st.selectbox("Модель для предсказания", list(models.keys()), label_visibility="collapsed")

# Загрузка выбранной модели
model = joblib.load(models[selected_model])

# Текстовое поле для ввода URL
st.subheader("Введите URL вакансии")
url = st.text_input("URL", placeholder="https://example.com/vacancy/123", label_visibility="collapsed")

# Обработка URL и предсказание
if url:
    with st.spinner("Обработка вакансии..."):
        try:
            # Парсинг данных
            vacancy_data = parse_vacancy(url)

            # Подготовка признаков
            features = prepare_features(vacancy_data)

            # Имитация задержки для демонстрации прогресс-бара
            # time.sleep(1)

            # Предсказание зарплаты
            # predicted_salary = model.predict(features)[0]  # Ожидается [salary_from, salary_to]
            delta = 30_000
            # salary_from, salary_to = predicted_salary - delta, predicted_salary + delta
            salary_from, salary_to = 10000000 - delta, 100000000 + delta

            # Вывод результатов
            st.subheader("Детали вакансии")
            st.markdown(f"""
            <div class="vacancy-box">
                <strong>Название:</strong> {vacancy_data['name']}<br>
                <strong>Описание:</strong> {vacancy_data['description']}<br>
                <strong>Предсказанный диапазон зарплаты (RUB):</strong> {salary_from:,.0f} - {salary_to:,.0f}
            </div>""", unsafe_allow_html=True)

            # Вывод результатов
            # st.subheader("Детали вакансии")
            # st.markdown(f"""
            #             <div
            #
            #
            # class ="vacancy-box">
            #
            # <strong> Название: </strong> {vacancy_data['name']} <br>
            # <strong> Описание: </strong> {vacancy_data['description']} <br>
            # <strong> Предсказанный
            # диапазон
            # зарплаты(RUB): </strong> {salary_from:, .0f} - {salary_to:, .0 f}
            # </div> """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Ошибка обработки URL: {str(e)}")
else:
    st.markdown(f"""
               <div class="vacancy-box">
                   <strong>Название:</strong> Введите    URL, чтобы    увидеть    детали вакансии<br>
                   <strong>Описание:</strong> Ожидание    ввода...<br>
                   <strong>Предсказанный диапазон зарплаты (RUB):</strong> Ожидание    ввода...
               </div>""", unsafe_allow_html=True)

# Закрытие основного контента
st.markdown('</div>', unsafe_allow_html=True)

# Футер
st.markdown("""
<div class ="footer">


Создано
студенткой
математического
факультета
СОГУ |
<a
href = "https://github.com/your-username"> GitHub </a> |
<a
href = "https://t.me/YourTelegram"> Telegram </a> <br>
Разработано
при
поддержке
xAI | Создано
с
использованием
Streamlit | Данные
обрабатываются
с
помощью
DuckDB
и
Random
Forest
</div>
""", unsafe_allow_html=True)
