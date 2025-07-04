import os

import streamlit as st
import joblib

from css_fro_streamlit import css
from models.model_2_architecture import Net
from prep_data_for_model import *
from transformers import AutoTokenizer, AutoModel

st.sidebar.page_link("streamlit_app.py", label="Главная")
st.sidebar.page_link("pages/1_Analytics.py", label="Анализ зарплат")
st.sidebar.page_link("pages/2_Salary_Prediction.py", label="Предсказание заработной платы")
st.sidebar.page_link("pages/3_Useful_info.py", label="Полезная информация")


@st.cache_resource
def get_mlb():
    return joblib.load('models/mlb_encoder.pkl')


@st.cache_resource
def get_tokenizer():
    try:
        tokenizer_ = AutoTokenizer.from_pretrained("./rubert_tokenizer2")
        return tokenizer_
    except:
        tokenizer_ = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
        tokenizer_.save_pretrained("./rubert_tokenizer2")
        return tokenizer_


@st.cache_resource
def get_rubert_model():
    try:
        model_ = AutoModel.from_pretrained("./rubert_model")
        return model_
    except:
        model_ = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")
        model_.save_pretrained("./rubert_model")
        return model_


def predict_salary_torch(name, description, experience_str,
                   tokenizer, model_rubert, model_net, device,
                   y_train_mean=127050.85983732407, y_train_std=74488.1467090772
                   ):
    """
    name, description: строки
    experience_str: строка из experience_mapping
    """
    # 👇 Правильно формируем входной текст — как в твоём пайплайне
    input_text = build_input2(name, description)

    # Получаем эмбеддинг через ruBERT
    model_rubert.eval()
    with torch.no_grad():
        inputs = tokenizer([input_text], return_tensors="pt", truncation=True, padding=True, max_length=512)
        outputs = model_rubert(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).cpu().numpy().ravel()

    # Опыт через mapping
    exp_val = experience_mapping.get(experience_str.strip(), 0)

    # Финальный вектор
    input_features = np.concatenate([embedding, [exp_val]], axis=0).astype(np.float32)

    # Прогон через сеть
    model_net.eval()
    with torch.no_grad():
        x_tensor = torch.tensor(input_features, dtype=torch.float32).unsqueeze(0).to(device)
        pred_scaled = model_net(x_tensor).cpu().numpy().ravel()[0]
        pred_rub = pred_scaled * y_train_std + y_train_mean

    return pred_rub


# Список доступных моделей
models = {
    "Случайный лес": "models/random_forest_model2.pkl",
    "Нейронная сеть (v1)": "models/model_NN_1_full.pt",
    "Нейронная сеть (v2)": "models/model_NN_2_full.pt"
}

# Кастомный CSS для стилизации
st.markdown(css, unsafe_allow_html=True)

# st.title("UCARY")

# tab1, tab2 = st.tabs(["Аналитика", "Предсказания🔮"])
# with tab1:
#     st.header("Туть аналитика")
# with tab2:
# Хедер
# st.header("Дашборд предсказания зарплаты")
st.markdown('<div class="header">Дашборд предсказания зарплаты</div>', unsafe_allow_html=True)

# Основной контент
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Выпадающий список для выбора модели
st.subheader("Выберите модель")
selected_model = st.selectbox("Модель для предсказания", list(models.keys()), label_visibility="collapsed")

# Загрузка выбранной модели
# model = joblib.load(models[selected_model])
selected_model_path = models[selected_model]
_, ext = os.path.splitext(selected_model_path)



# Загружаем модель по расширению
if ext == ".pkl":
    model = joblib.load(selected_model_path)
elif ext == ".pt":
    model = Net(769)
    # model.load_state_dict(torch.load(selected_model_path, weights_only=True))
    model = torch.load(selected_model_path, weights_only=False)
    model.eval()
else:
    st.error(f"❌ Неподдерживаемый формат модели: {ext}")
    st.stop()

mlb = get_mlb()
tokenizer = get_tokenizer()
model_rubert = get_rubert_model()

# Текстовое поле для ввода URL
st.subheader("Введите URL вакансии")

st.text("Url для примера:")
st.code("https://vladikavkaz.hh.ru/vacancy/116838770", language='text')
url = st.text_input("URL", placeholder="https://vladikavkaz.hh.ru/vacancy/id", label_visibility="collapsed")

# Обработка URL и предсказание
if url:
    with st.spinner("Обработка вакансии..."):
        try:
            # Парсинг данных
            api_url = convert_hh_url_to_api(url)
            vacancy_data = parse_vacancy(api_url)

            # Предсказание зарплаты
            if ext == ".pkl":
                # Подготовка признаков
                features = prepare_features(vacancy_data, mlb, tokenizer, model_rubert)

                predicted_salary = model.predict(features)[0]
            elif ext == ".pt":
                predicted_salary = predict_salary_torch(
                    safe_get(vacancy_data, "name", ""),
                    safe_get(vacancy_data, "description", ""),
                    experience_mapping.get(safe_get(safe_get(vacancy_data, "experience", {}), "name", ""), 1),
                    tokenizer, model_rubert, model,
                    device=torch.device("cpu"),
                )

            delta = 30_000 // 2
            salary_from, salary_to = predicted_salary - delta, predicted_salary + delta

            # Вывод результатов
            st.subheader("Результаты и Детали вакансии")
            sf = safe_get(safe_get(vacancy_data, "salary", {}), "from", None)
            st_ = safe_get(safe_get(vacancy_data, "salary", {}), "to", None)
            original_salary_html = ""
            if sf is not None and st_ is not None:
                original_salary_html = f"{sf:,.0f} - {st_:,.0f}"

            elif sf is not None:
                original_salary_html = f"{sf:,.0f} - ?"

            elif st_ is not None:
                original_salary_html = f" ? - {st_:,.0f}"
            else:
                "Не указан"
            st.markdown(f"""
            <div class="vacancy-box">
                <strong>Предсказанный диапазон зарплаты (RUB):</strong> {salary_from:,.0f} - {salary_to:,.0f}<br>
                <strong>Оригинальный диапазон зарплаты (RUB):</strong> {original_salary_html} <br>
                <br>
                <strong>Название:</strong> {vacancy_data['name']}<br>
                <strong>Описание:</strong> {vacancy_data['description']}<br>
            </div>""", unsafe_allow_html=True)

        except Exception as e:
            print(e)
            st.error(f"Ошибка обработки URL: {str(e)}")
else:
    st.markdown(f"""
               <div class="vacancy-box">
                   <strong>Предсказанный диапазон зарплаты (RUB):</strong> Ожидание    ввода... <br>
                   <strong>Название:</strong> Введите    URL, чтобы    увидеть    детали вакансии<br>
                   <strong>Описание:</strong> Ожидание    ввода...<br>
               </div>""", unsafe_allow_html=True)

# Закрытие основного контента
st.markdown('</div>', unsafe_allow_html=True)

# Футер
st.markdown("""
<div class ="footer">
    Создано студенткой матфака СОГУ |
    <a href = "https://github.com/Lana-Dzuceva"> GitHub </a> |
    <a href = "https://t.me/Lana_hmm"> Telegram </a> <br>
    Разработано при поддержке xAI | Создано с использованием
    Streamlit | Данные обрабатываются
    с помощью DuckDB
    и Random Forest
</div>
""", unsafe_allow_html=True)

# Имитация задержки
# time.sleep(1)