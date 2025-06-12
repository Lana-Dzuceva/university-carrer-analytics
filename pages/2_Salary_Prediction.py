# import streamlit as st
# import joblib
#
# from css_fro_streamlit import css
# from prep_data_for_model import *
# from transformers import AutoTokenizer, AutoModel
#
#
# @st.cache_resource
# def get_mlb():
#     return joblib.load('models/mlb_encoder.pkl')
#
#
# @st.cache_resource
# def get_tokenizer():
#     try:
#         tokenizer_ = AutoTokenizer.from_pretrained("./rubert_tokenizer2")
#         return tokenizer_
#     except:
#         tokenizer_ = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
#         tokenizer_.save_pretrained("./rubert_tokenizer2")
#         return tokenizer_
#
#
# @st.cache_resource
# def get_rubert_model():
#     try:
#         model_ = AutoModel.from_pretrained("./rubert_model")
#         return model_
#     except:
#         model_ = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")
#         model_.save_pretrained("./rubert_model")
#         return model_
#
#
# # Список доступных моделей
# models = {
#     "Случайный лес (v2)": "models/random_forest_model2.pkl",
#     "Случайный лес (v1)": "models/random_forest_model2.pkl"  # Замените на реальные имена файлов
# }
#
# # Кастомный CSS для стилизации
# st.markdown(css, unsafe_allow_html=True)
#
# st.title("UCARY")
#
# tab1, tab2 = st.tabs(["Аналитика", "Предсказания🔮"])
# with tab1:
#     st.header("Туть аналитика")
# with tab2:
#     # Хедер
#     # st.header("Дашборд предсказания зарплаты")
#     st.markdown('<div class="header">Дашборд предсказания зарплаты</div>', unsafe_allow_html=True)
#
#     # Основной контент
#     st.markdown('<div class="main-content">', unsafe_allow_html=True)
#
#     # Выпадающий список для выбора модели
#     st.subheader("Выберите модель")
#     selected_model = st.selectbox("Модель для предсказания", list(models.keys()), label_visibility="collapsed")
#
#     # Загрузка выбранной модели
#     model = joblib.load(models[selected_model])
#     mlb = get_mlb()
#     tokenizer = get_tokenizer()
#     model_rubert = get_rubert_model()
#
#     # Текстовое поле для ввода URL
#     st.subheader("Введите URL вакансии")
#     st.text("Url для примера https://vladikavkaz.hh.ru/vacancy/116838770")
#     url = st.text_input("URL", placeholder="https://vladikavkaz.hh.ru/vacancy/116838770", label_visibility="collapsed")
#
#     # Обработка URL и предсказание
#     if url:
#         with st.spinner("Обработка вакансии..."):
#             try:
#                 # Парсинг данных
#                 api_url = convert_hh_url_to_api(url)
#                 vacancy_data = parse_vacancy(api_url)
#
#                 # Подготовка признаков
#                 features = prepare_features(vacancy_data, mlb, tokenizer, model_rubert)
#
#                 # Имитация задержки для демонстрации прогресс-бара
#                 # time.sleep(1)
#
#                 # Предсказание зарплаты
#                 predicted_salary = model.predict(features)[0]
#                 delta = 30_000 // 2
#                 salary_from, salary_to = predicted_salary - delta, predicted_salary + delta
#
#                 # Вывод результатов
#                 # st.subheader("")
#                 st.subheader("Результаты и Детали вакансии")
#                 sf = safe_get(safe_get(vacancy_data, "salary", {}), "from", None)
#                 st_ = safe_get(safe_get(vacancy_data, "salary", {}), "to", None)
#                 original_salary_html = ""
#                 if sf is not None and st_ is not None:
#                     original_salary_html = f"{sf:,.0f} - {st_:,.0f}"
#
#                 elif sf is not None:
#                     original_salary_html = f"{sf:,.0f} - ?"
#
#                 elif st_ is not None:
#                     original_salary_html = f" ? - {st_:,.0f}"
#                 else:
#                     "Не указан"
#                 st.markdown(f"""
#                 <div class="vacancy-box">
#                     <strong>Предсказанный диапазон зарплаты (RUB):</strong> {salary_from:,.0f} - {salary_to:,.0f}<br>
#                     <strong>Оригинальный диапазон зарплаты (RUB):</strong> {original_salary_html} <br>
#                     <br>
#                     <strong>Название:</strong> {vacancy_data['name']}<br>
#                     <strong>Описание:</strong> {vacancy_data['description']}<br>
#                 </div>""", unsafe_allow_html=True)
#
#             except Exception as e:
#                 print(e)
#                 st.error(f"Ошибка обработки URL: {str(e)}")
#     else:
#         st.markdown(f"""
#                    <div class="vacancy-box">
#                        <strong>Предсказанный диапазон зарплаты (RUB):</strong> Ожидание    ввода... <br>
#                        <strong>Название:</strong> Введите    URL, чтобы    увидеть    детали вакансии<br>
#                        <strong>Описание:</strong> Ожидание    ввода...<br>
#                    </div>""", unsafe_allow_html=True)
#
#     # Закрытие основного контента
#     st.markdown('</div>', unsafe_allow_html=True)
#
#     # Футер
#     st.markdown("""
#     <div class ="footer">
#         Создано студенткой матфака СОГУ |
#         <a href = "https://github.com/Lana-Dzuceva"> GitHub </a> |
#         <a href = "https://t.me/Lana_hmm"> Telegram </a> <br>
#         Разработано при поддержке xAI | Создано с использованием
#         Streamlit | Данные обрабатываются
#         с помощью DuckDB
#         и Random Forest
#     </div>
#     """, unsafe_allow_html=True)
