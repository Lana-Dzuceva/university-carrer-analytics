import mysql.connector
import json
from datetime import datetime
from utils import *

def insert_all_vacancies(vacancies):
    conn = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="1234",
        database="hh_data"
    )
    for vac in vacancies:
        try:
            insert_vacancy(vac, conn)
        except Exception:
            print("--------------------------------EXCEPTION------------------------------------------")
            print(str(Exception))
            print("--------------------------------------------------------------------------")

    conn.close()

def insert_vacancy(vacancy: dict, connection):
    cursor = connection.cursor()

    formatted_time = vacancy.get("published_at", "")
    try:
        formatted_time = datetime.fromisoformat(formatted_time.replace("Z", "+00:00"))
    except:
        formatted_time = datetime.now()

    key_skills = [skill["name"] for skill in vacancy.get("key_skills", [])]
    key_skills_json = json.dumps(key_skills, ensure_ascii=False)

    values = (
        vacancy.get("id"),
        safe_get(vacancy, "name", ""),
        safe_get(vacancy, "premium", False),
        safe_get(safe_get(vacancy, "billing_type", {}), "name", ""),
        safe_get(safe_get(vacancy, "area", {}), "id", ""),
        safe_get(safe_get(vacancy, "area", {}), "name", ""),
        safe_get(safe_get(vacancy, "salary", {}), "from", None),
        safe_get(safe_get(vacancy, "salary", {}), "to", None),
        safe_get(safe_get(vacancy, "salary", {}), "currency", ""),
        safe_get(safe_get(vacancy, "salary", {}), "gross", None),
        # safe_get(safe_get(vacancy, "type", {}), "name", ""),
        safe_get(safe_get(vacancy, "address", {}), "city", ""),
        safe_get(safe_get(vacancy, "address", {}), "street", ""),
        safe_get(safe_get(vacancy, "address", {}), "building", ""),
        safe_get(safe_get(vacancy, "address", {}), "lat", None),
        safe_get(safe_get(vacancy, "address", {}), "lng", None),
        safe_get(safe_get(vacancy, "experience", {}), "name", ""),
        safe_get(safe_get(vacancy, "schedule", {}), "name", ""),
        safe_get(safe_get(vacancy, "employment", {}), "name", ""),
        safe_get(safe_get(vacancy, "employer", {}), "id", ""),
        safe_get(safe_get(vacancy, "employer", {}), "name", ""),
        safe_get(safe_get(vacancy, "employer", {}), "url", ""),
        formatted_time,
        safe_get(vacancy, "description", ""),
        safe_get(vacancy, "group_tag", ""),
        key_skills_json
    )

    insert_sql = """
    INSERT INTO vacancies (
        id_vacancy, name, premium, billing_type, area_id, area_name, salary_from, salary_to, salary_currency,
        salary_gross, type, city, street, lat, lng, experience, schedule, employment,
        employer_id, employer_name, employer_url, published_at, description, group_tag, key_skills
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_sql, values)
    connection.commit()
    cursor.close()