import duckdb
import json
from datetime import datetime
from utils import safe_get


def create_db():
    # Подключение к DuckDB (создаст файл, если его нет)
    conn = duckdb.connect("hh_vacancies.db")

    # Создание таблицы
    conn.execute("""
    CREATE SEQUENCE seq_vacancy_id START 1;
    
    CREATE TABLE IF NOT EXISTS vacancies (
        id INT PRIMARY KEY,
        id_vacancy VARCHAR,
        name VARCHAR,
        premium BOOLEAN,
        billing_type VARCHAR,
        area_id VARCHAR,
        area_name VARCHAR,
        salary_from INT,
        salary_to INT,
        salary_currency VARCHAR,
        salary_gross BOOLEAN,
        type VARCHAR,
        city VARCHAR,
        street VARCHAR,
        building VARCHAR,
        lat DOUBLE,
        lng DOUBLE,
        experience VARCHAR,
        schedule VARCHAR,
        employment VARCHAR,
        employer_id VARCHAR,
        employer_name VARCHAR,
        employer_url VARCHAR,
        published_at TIMESTAMP,
        description TEXT,
        key_skills TEXT
    );
    """)

    conn.close()


# Функция для загрузки JSON в базу
def insert_vacancies(json_data):
    conn = duckdb.connect("hh_vacancies.db")
    for vacancy in json_data:
        dt = datetime.strptime(vacancy.get("published_at"), "%Y-%m-%dT%H:%M:%S%z")
        # Преобразование в UTC (опционально)
        # dt_utc = dt.astimezone(tz=None)  # или явно указать timezone.utc
        # Форматирование для DuckDB (без временной зоны)
        formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
        formatted_time = formatted_time or '2025-03-30 12:00:00'

        s = f"""
        INSERT INTO vacancies  (
        id, id_vacancy, name, premium, billing_type, area_id, area_name, salary_from, salary_to, salary_currency, 
        salary_gross, type, city, street, building, lat, lng, experience, schedule, employment, 
        employer_id, employer_name, employer_url, published_at, description, key_skills
        )  VALUES (
        nextval('seq_vacancy_id'), щ
        '{vacancy.get("id")}', 
        '{safe_get(vacancy, "name", "")}',
        {safe_get(vacancy, "premium", 'FALSE')},
        '{safe_get(safe_get(vacancy, "billing_type", {}), "name", "")}',
        '{safe_get(safe_get(vacancy, "area", {}), "id", "")}',
        '{safe_get(safe_get(vacancy, "area", {}), "name", "")}',
        {safe_get(safe_get(vacancy, "salary", {}), "from", 'null')},
        {safe_get(safe_get(vacancy, "salary", {}), "to", 'null')},
        '{safe_get(safe_get(vacancy, "salary", {}), "currency", "")}',
        {safe_get(safe_get(vacancy, "salary", {}), "gross", 'null')},
        '{safe_get(safe_get(vacancy, "type", {}), "name", "")}',
        '{safe_get(safe_get(vacancy, "address", {}), "city", "")}',
        '{safe_get(safe_get(vacancy, "address", {}), "street", "")}',
        '{safe_get(safe_get(vacancy, "address", {}), "building", "")}',
        {safe_get(safe_get(vacancy, "address", {}), "lat", 'null')},
        {safe_get(safe_get(vacancy, "address", {}), "lng", 'null')},
        '{safe_get(safe_get(vacancy, "experience", {}), "name", "")}',
        '{safe_get(safe_get(vacancy, "schedule", {}), "name", "")}',
        '{safe_get(safe_get(vacancy, "employment", {}), "name", "")}',
        '{safe_get(safe_get(vacancy, "employer", {}), "id", "")}',
        '{safe_get(safe_get(vacancy, "employer", {}), "name", "")}',
        '{safe_get(safe_get(vacancy, "employer", {}), "url", "")}',
        '{formatted_time}',
        '{safe_get(vacancy, "description", "some_description")}'
        '{", ".join(skill["name"] for skill in vacancy.get("key_skills", [])) or "some_skill"}'
        );"""
        # ,
        # {", ".join(skill["name"] for skill in vacancy.get("key_skills", []))}
        # a = """
        #  INSERT INTO hh_vacancies.main.vacancies (
        # id, id_vacancy, name, premium, billing_type, area_id, area_name, salary_from, salary_to, salary_currency,
        # salary_gross, type, city, street, building, lat, lng, experience, schedule, employment,
        # employer_id, employer_name, employer_url, published_at, description, key_skills
        # ) VALUES (
        #     nextval('seq_vacancy_id'),  -- Используем последовательность для id
        #     '6969',
        #     'Stas',
        #     FALSE,
        #     'Fixed',
        #     '1',
        #     'Moscow',
        #     100000,
        #     150000,
        #     'RUB',
        #     TRUE,
        #     'Full-time',
        #     'Moscow',
        #     'Lenina',
        #     '10',
        #     55.7558,
        #     37.6173,
        #     '3-6 years',
        #     'Full Day',
        #     'Permanent',
        #     '78910',
        #     'Tech Corp',
        #     'https://techcorp.com',
        #     '2025-03-30 12:00:00',
        #     'Great job opportunity for experienced developers.',
        #     'Python, SQL, Machine Learning'
        # );
        # """
        try:
            conn.execute(s)
        except:
            pass
    conn.close()


# Читаем JSON и вставляем в базу
# with open("vacancies.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#     insert_vacancies(data)
#


def insert_vacancies2(vacancies: list):
    conn = duckdb.connect("vacancies.duckdb")
    for vac in vacancies:
        try:
            insert_vacancy2(vac, conn)
        except duckdb.InvalidInputException as e:
            print(str(e))
        except Exception as e:
            print(e)
    conn.close()


def insert_vacancy2(vacancy: dict, connection):
    key_skills = [skill["name"] for skill in vacancy.get("key_skills", [])]
    group_tag = vacancy.get("group_tag", "")
    params = [
        safe_get(vacancy, "id", ""),
        safe_get(vacancy, "name", ""),
        safe_get(vacancy, "premium", False),
        safe_get(safe_get(vacancy, "billing_type", {}), "name", ""),
        safe_get(safe_get(vacancy, "area", {}), "id", ""),
        safe_get(safe_get(vacancy, "area", {}), "name", ""),
        safe_get(safe_get(vacancy, "salary", {}), "from", None),
        safe_get(safe_get(vacancy, "salary", {}), "to", None),
        safe_get(safe_get(vacancy, "salary", {}), "currency", ""),
        safe_get(safe_get(vacancy, "salary", {}), "gross", None),
        safe_get(safe_get(vacancy, "type", {}), "name", ""),
        safe_get(safe_get(vacancy, "address", {}), "city", None),
        safe_get(safe_get(vacancy, "address", {}), "street", None),
        safe_get(safe_get(vacancy, "address", {}), "lat", None),
        safe_get(safe_get(vacancy, "address", {}), "lng", None),
        safe_get(safe_get(vacancy, "experience", {}), "name", ""),
        safe_get(safe_get(vacancy, "schedule", {}), "name", ""),
        safe_get(safe_get(vacancy, "employment", {}), "name", ""),
        safe_get(safe_get(vacancy, "employer", {}), "id", ""),
        safe_get(safe_get(vacancy, "employer", {}), "name", ""),
        safe_get(safe_get(vacancy, "employer", {}), "url", ""),
        safe_get(vacancy, "published_at", None),
        safe_get(vacancy, "description", ""),
        key_skills,
        group_tag,
        datetime.today()
    ]

    # insert_sql = f"""
    #     INSERT INTO vacancies (
    #         id_vacancy, name, premium, billing_type, area_id, area_name,
    #         salary_from, salary_to, salary_currency, salary_gross, type,
    #         city, street, lat, lng, experience, schedule, employment,
    #         employer_id, employer_name, employer_url, published_at,
    #         description, key_skills, group_tag
    #     ) VALUES ({', '.join('?' * len(params))})
    # """
    # print('SQL Preview:\n', insert_sql)
    rel = connection.table('vacancies')
    rel.insert(params)
    # print("inserted  " + str(params[1]))
    # connection.execute(insert_sql, params)


def check_data():
    conn = duckdb.connect("hh_vacancies.db")
    # Проверка вставленных данных
    print(conn.execute("SELECT * FROM vacancies LIMIT 5").fetchall())
    conn.close()
