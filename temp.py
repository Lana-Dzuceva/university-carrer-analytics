import json

import duckdb
import requests

# парсю все регионы с hh.ru
# with open("areas.json", "w", encoding="utf-8") as json_file:
#     areas_url = "https://api.hh.ru/areas"
#     areas = requests.get(areas_url).json()
#     areas_ids = [(area['id'], area['name']) for area in areas[0]['areas']]  # id регионов рф
#     json.dump(areas_ids, json_file, ensure_ascii=False, indent=4)
#     area = 113
#     print(f"Данные успешно сохранены в файл areas.json")

# from transformers import AutoModel, AutoTokenizer
# model = AutoModel.from_pretrained("DeepPavlov/rubert-base-cased")
# tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
# model.save_pretrained("/rubert_model")
# tokenizer.save_pretrained("/rubert_tokenizer2")

# duckdb.sql(r'LOAD motherduck FROM "C:\Users\admin\Downloads\motherduck.duckdb_extension"')
# import duckdb
# duckdb.sql("""
#     INSTALL motherduck FROM 'https://extensions.duckdb.org/v1.3.0/windows_amd64/motherduck.duckdb_extension.gz';
# """)


import plotly.express as px
import pandas as pd

# Данные
data = {
    "Платформа": ["HH.ru", "Работа.ру", "Хабр Карьера", "Карьерист", "Job Lab", "SuperJob", "Trudvsem"],
    "Вакансии": [1164544, 250000, 2835, 1083082, 300000, 500000, 1746772]
}

df = pd.DataFrame(data)

# Построение графика с разными цветами
fig = px.bar(
    df,
    x="Платформа",
    y="Вакансии",
    text="Вакансии",
    color="Платформа",  # !!! ключевой момент: цвет зависит от платформы
    title="📊 Количество вакансий по разным платформам",
    labels={"Вакансии": "Количество вакансий"}
)

# Форматирование текста
fig.update_traces(
    texttemplate='%{text:,}',  # 1 000 000 вместо 1000000
    textposition='outside'
)

fig.update_layout(
    xaxis_tickangle=-30,
    yaxis_title="Количество вакансий",
    xaxis_title="Платформа",
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    showlegend=False  # опционально, можно убрать легенду
)

fig.show()
