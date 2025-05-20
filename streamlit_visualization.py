import streamlit as st
import duckdb
import pandas as pd
import altair as alt

# Заголовок
st.title("📊 Анализ зарплат по вакансиям")

# Подключение к DuckDB
con = duckdb.connect("vacancies.duckdb")


# Загружаем данные
@st.cache_data
def load_data():
    query = """
    SELECT 
        salary_from, salary_to, area_name, name, published_at
    FROM vacancies
    WHERE salary_from IS NOT NULL
    """
    return con.execute(query).df()


df = load_data()

# Очищаем данные
df = df[df['salary_from'] > 0]
df['published_at'] = pd.to_datetime(df['published_at'])

# Фильтрация по региону
regions = df['area_name'].dropna().unique().tolist()
selected_region = st.selectbox("Выбери регион:", ["Все"] + sorted(regions))

if selected_region != "Все":
    df = df[df['area_name'] == selected_region]

# 📈 График 1: распределение зарплат (гистограмма)
st.subheader("Распределение нижней границы зарплат")
hist_chart = alt.Chart(df).mark_bar().encode(
    alt.X("salary_from", bin=alt.Bin(maxbins=30), title="Зарплата от (RUR)"),
    y="count()",
).properties(width=700, height=400)
st.altair_chart(hist_chart)

# 📊 График 2: средняя ЗП по регионам
st.subheader("Средняя зарплата по регионам")
region_salary_df = (
    df.groupby("area_name")["salary_from"]
    .mean()
    .reset_index()
    .rename(columns={"salary_from": "avg_salary"})
)

bar_chart = alt.Chart(region_salary_df).mark_bar().encode(
    x=alt.X("avg_salary", title="Средняя зарплата"),
    y=alt.Y("area_name", sort="-x", title="Регион"),
).properties(width=700, height=500)
st.altair_chart(bar_chart)

# 📆 График 3: динамика публикаций вакансий
st.subheader("Динамика вакансий по дате публикации")
time_df = (
    df.groupby(df['published_at'].dt.date)['salary_from']
    .count()
    .reset_index()
    .rename(columns={"salary_from": "vacancy_count", "published_at": "date"})
)

line_chart = alt.Chart(time_df).mark_line(point=True).encode(
    x="date:T",
    y="vacancy_count:Q"
).properties(width=700, height=400)

st.altair_chart(line_chart)
