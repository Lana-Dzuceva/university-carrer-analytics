import numpy as np
import requests
import torch

from utils import safe_get


# Функция для парсинга
def parse_vacancy(url):
    """
    Принимает URL вакансии и возвращает данные для модели.
    """
    try:
        response = requests.get(url)

        if response.status_code == 200:
            vacancy_details = response.json()
            return vacancy_details
    except Exception as e:
        print(e)


# Функция для подготовки признаков
def prepare_features(data, mlb, tokenizer, model_for_embedding):
    """
    Преобразует данные в формат, подходящий для модели.
    - mlb
     Параметры: TODO подписать параметры
    - input_text (str): Текст (например, описание вакансии или резюме).
    - key_skills (list): Список навыков (например, ['Python', 'SQL']).
    - experience (str): Уровень опыта ('No experience', 'Junior', 'Middle', 'Senior').
    - tokenizer: Токенизатор RuBERT.
    - model: Модель RuBERT.
    - mlb: MultiLabelBinarizer для one-hot encoding навыков.
    - rf: Обученная модель RandomForestRegressor.
    - device (str): Устройство для RuBERT ('cuda' или 'cpu').

    Возвращает:
    - float: Предсказанная зарплата.
    """
    experience = safe_get(safe_get(data, "experience", {}), "name", "")
    # 1. Преобразование experience в числовое значение
    experience_mapping = {'Нет опыта': 1, 'От 1 года до 3 лет': 2, 'От 3 до 6 лет': 3, 'Более 6 лет': 4}
    experience_numeric = experience_mapping.get(experience, 1)  # По умолчанию 1, если значение неизвестно

    input_text = build_input(data)
    # 2. Получение эмбеддинга RuBERT для текста
    embeddings = get_rubert_embeddings([input_text], tokenizer, model_for_embedding, max_length=512, batch_size=1)

    # 3. One-hot encoding для key_skills
    key_skills = [skill["name"] for skill in data.get("key_skills", [])]
    skills_lower = [skill.lower() for skill in key_skills]
    skills_encoded = mlb.transform([skills_lower])

    return [data["description"]]


def predict_salary(input_text, key_skills, experience, tokenizer, model, mlb, rf, device='cpu'):
    """
    Предсказывает зарплату на основе текста, навыков и опыта.

    Параметры:
    - input_text (str): Текст (например, описание вакансии или резюме).
    - key_skills (list): Список навыков (например, ['Python', 'SQL']).
    - experience (str): Уровень опыта ('No experience', 'Junior', 'Middle', 'Senior').
    - tokenizer: Токенизатор RuBERT.
    - model: Модель RuBERT.
    - mlb: MultiLabelBinarizer для one-hot encoding навыков.
    - rf: Обученная модель RandomForestRegressor.
    - device (str): Устройство для RuBERT ('cuda' или 'cpu').

    Возвращает:
    - float: Предсказанная зарплата.
    """

    # 3. One-hot encoding для key_skills
    skills_lower = [skill.lower() for skill in key_skills]
    skills_encoded = mlb.transform([skills_lower])

    # 4. Объединение признаков
    X = np.hstack([
        embeddings,  # RuBERT эмбеддинги
        np.array([[experience_numeric]]),  # Числовой опыт
        skills_encoded  # One-hot encoded навыки
    ])

    # 5. Предсказание
    prediction = rf.predict(X)
    return prediction[0]


def build_input(data):
    temp = f'''[TITLE] {safe_get(data, "name", "")}'''
    key_skills = [skill["name"] for skill in data.get("key_skills", [])]
    skills = ', '.join(key_skills)
    if skills:
        temp += f" [SKILLS] {skills}"
    temp += f" [DESC] {data['description']}"
    return temp


# Функция для получения эмбеддингов RuBERT
def get_rubert_embeddings(texts, tokenizer, model, max_length=512, batch_size=8):
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        inputs = tokenizer(batch_texts, return_tensors="pt", max_length=max_length,
                           truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        # Берем эмбеддинги [CLS] токена (первый токен)
        batch_embeddings = outputs.last_hidden_state[:, 0, :].numpy()
        embeddings.append(batch_embeddings)
    return np.vstack(embeddings)
