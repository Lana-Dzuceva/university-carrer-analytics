import duckdb
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from css_fro_streamlit import css
import altair as alt

st.set_page_config(
    # layout="wide",
    initial_sidebar_state="expanded",
)
# Кастомный CSS для стилизации
st.markdown(css, unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.title("Аналитика вакансий со всей России")

# Подключение к DuckDB
# os.environ['MOTHERDUCK_TOKEN'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImxhbmFkenVjZXZhQGdtYWlsLmNvbSIsInNlc3Npb24iOiJsYW5hZHp1Y2V2YS5nbWFpbC5jb20iLCJwYXQiOiJsNV8zUWI4eDVHYjVKSlVMNE1OZ1J5TmxVQlhCeWRHUzFsUFhEekNHZzVBIiwidXNlcklkIjoiYWNkOGQ1YmItYzEwZS00NmU5LWI1MDYtMmY2MDMxMWQ1MDhhIiwiaXNzIjoibWRfcGF0IiwicmVhZE9ubHkiOmZhbHNlLCJ0b2tlblR5cGUiOiJyZWFkX3dyaXRlIiwiaWF0IjoxNzQ3NjgzOTM5fQ.BMAAlTiKwUcvcYytiuc3_YqICTJpmEfHYPPYjEf7Z6s'


@st.cache_resource
def get_connection():
    return duckdb.connect("vacancies.duckdb")  # duckdb.connect('md:vacancies_')


con = get_connection()

query = f"""
    SELECT * FROM vacancies
   
"""
#  WHERE group_tag IN ({','.join([f"'{tag}'" for tag in selected_tags])})
#     AND experience IN ({','.join([f"'{exp}'" for exp in selected_experience])})
#     AND city IN ({','.join([f"'{city}'" for city in selected_cities])})
#     AND schedule IN ({','.join([f"'{sch}'" for sch in selected_schedules])})
#     AND employment IN ({','.join([f"'{emp}'" for emp in selected_employment])})
df = con.execute(query).fetchdf()

# region Географическое распределение
st.subheader("Географическое распределение")
if not df[['lat', 'lng']].isna().all().all():
    fig_map = px.scatter_map(
        df,
        lat="lat",
        lon="lng",
        hover_name="name",
        hover_data=["city", "salary_from", "experience"],
        zoom=5,
        height=500
    )
    fig_map.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_map)
else:
    st.write("Нет данных о координатах для выбранных вакансий.")

# endregion


# region part-time work
# st.subheader("🗂️ Варианты занятости в данных")
#
# employment_counts = df['employment'].fillna('Не указано').value_counts().reset_index()
# employment_counts.columns = ['Тип занятости', 'Количество']
#
# st.dataframe(employment_counts, use_container_width=True)

with st.expander("📌 Вакансии с частичной занятостью"):
    total_vacancies = len(df)
    part_time_vacancies = df[df['employment'] == 'Частичная занятость']
    part_time_count = len(part_time_vacancies)

    if total_vacancies > 0:
        percent = round(part_time_count / total_vacancies * 100, 2)
    else:
        percent = 0.0

    st.markdown(f"""
    **Частичная занятость**:
    - 🧾 Количество: **{part_time_count:,}**
    - 📊 Процент от всех вакансий: **{percent}%**
    """)

# endregion


# region Распределение зарплат по группам (с учётом расчёта target_salary)
st.subheader("📦 Распределение зарплат по группам")
mean_salary_fork = 30_000


def calculate_target_salary(row):
    salary_from = row['salary_from']
    salary_to = row['salary_to']

    if pd.notna(salary_from) and pd.notna(salary_to):
        target_salary = (salary_from + salary_to) / 2
    elif pd.notna(salary_from):
        target_salary = salary_from + mean_salary_fork // 2
    elif pd.notna(salary_to):
        target_salary = salary_to - mean_salary_fork // 2
    else:
        # return np.nan
        target_salary = np.nan
    return target_salary


df['target_salary'] = df.apply(calculate_target_salary, axis=1)

box_df = df.dropna(subset=['target_salary', 'group_tag'])

fig = px.box(
    box_df,
    x='group_tag',
    y='target_salary',
    color='group_tag',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    points='outliers',
    # title="📦 Распределение зарплат по группам"
)

fig.update_layout(
    xaxis_title="Группа (group_tag)",
    yaxis_title="Целевая зарплата",
    yaxis=dict(range=[0, 800000]),
    showlegend=False,
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# endregion


# region Типы занятости Pie
# Заменим пропущенные значения на "Не указано"
df['schedule_clean'] = df['schedule'].fillna('Не указано')

# Посчитаем количество каждой категории
schedule_counts = df['schedule_clean'].value_counts().reset_index()
schedule_counts.columns = ['Тип занятости (schedule)', 'Количество вакансий']

# 📊 Таблица
# st.subheader("Тип занятости: Таблица распределения")
# st.dataframe(schedule_counts, use_container_width=True)

# 🥧 Круговая диаграмма (pie chart)
st.subheader("Тип занятости: Круговая диаграмма")
fig = px.pie(
    schedule_counts,
    names='Тип занятости (schedule)',
    values='Количество вакансий',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    hole=0.3
)
st.plotly_chart(fig, use_container_width=True)

# endregion


# region Удалёнка vs Офис (обновлено с target_salary)
st.subheader("Удалёнка vs Офис")

# Заполним schedule и отфильтруем нужные категории
df['schedule_clean'] = df['schedule'].fillna('Не указано')
valid_schedules = ['Полный день', 'Удаленная работа']
filtered_df = df[df['schedule_clean'].isin(valid_schedules)]

# Группировка с использованием target_salary
summary = filtered_df.groupby('schedule_clean').agg({
    'id_vacancy': 'count',
    'target_salary': 'median'
}).rename(columns={
    'id_vacancy': 'Количество вакансий',
    'target_salary': 'Медианная зарплата'
}).reset_index().rename(columns={'schedule_clean': 'Тип'})

# Цвета Pastel
pastel_colors = px.colors.qualitative.Pastel
while len(pastel_colors) < summary.shape[0]:
    pastel_colors += pastel_colors  # Продублируем при необходимости

# Столбцы с графиками
col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Количество вакансий по типу занятости")
    chart1 = alt.Chart(summary).mark_bar().encode(
        x=alt.X('Тип:N', title=None),
        y=alt.Y('Количество вакансий:Q'),
        color=alt.Color('Тип:N', scale=alt.Scale(range=pastel_colors), legend=None),
        tooltip=['Тип', 'Количество вакансий']
    ).properties(height=350)
    st.altair_chart(chart1, use_container_width=True)

with col2:
    st.markdown("##### Медианная зарплата по типу занятости")
    chart2 = alt.Chart(summary).mark_bar().encode(
        x=alt.X('Тип:N', title=None),
        y=alt.Y('Медианная зарплата:Q'),
        color=alt.Color('Тип:N', scale=alt.Scale(range=pastel_colors), legend=None),
        tooltip=['Тип', 'Медианная зарплата']
    ).properties(height=350)
    st.altair_chart(chart2, use_container_width=True)
# endregion


# region Топ 25 ключевых навыков
st.subheader("🎯 Топ-25 ключевых навыков")

col1, col2 = st.columns(2)

with col1:
    exp_filter = st.selectbox(
        "Фильтр по опыту",
        options=["Все"] + df['experience'].dropna().unique().tolist()
    )

with col2:
    group_filter = st.selectbox(
        "Фильтр по группе (group_tag)",
        options=["Все"] + df['group_tag'].dropna().unique().tolist()
    )

# 📋 Фильтрация датафрейма
filtered_df = df.copy()
if exp_filter != "Все":
    filtered_df = filtered_df[filtered_df['experience'] == exp_filter]
if group_filter != "Все":
    filtered_df = filtered_df[filtered_df['group_tag'] == group_filter]

# 💰 Средняя зарплата по фильтрам
mean_salary = filtered_df['target_salary'].mean()
if pd.notna(mean_salary):
    st.markdown(
        f"📌 **Средняя зарплата по фильтрам**: **{int(mean_salary):,} ₽**"
    )
# else:
#     st.markdown("📌 **Недостаточно данных для расчёта средней зарплаты.**")

# 🧮 Подсчёт топ-25 навыков
top_skills = (
    filtered_df['key_skills']
    .explode()
    .value_counts()
    .head(25)
    .reset_index()
)
top_skills.columns = ['Навык', 'Количество']

fig = px.bar(
    top_skills.sort_values('Количество', ascending=False),
    x='Количество',
    y='Навык',
    orientation='h',
    color='Навык',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title='Топ-25 ключевых навыков',
    height=600
)
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)
# endregion


# region Дата последнего обновления
df['date_inserted'] = pd.to_datetime(df['date_inserted'], errors='coerce')

last_update = df['date_inserted'].max()

if pd.notnull(last_update):
    st.markdown(f"🕒 **Последнее обновление данных:** {last_update.strftime('%d.%m.%Y')}")
# else:
#     st.warning("Не удалось определить дату последнего обновления.")

# endregion

st.markdown('</div>', unsafe_allow_html=True)
