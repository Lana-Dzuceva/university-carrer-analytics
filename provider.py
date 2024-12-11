import json

import requests

from constants import PROFESSIONAL_ROLES, VACANCY_TITLES


def get_query_parameters(title, area, page):
    par2 = [('text', title), ('area', area), ('per_page', '20'), ('page', page)]
    par2.extend(PROFESSIONAL_ROLES)
    return


def get_1_vacancy(title, area=113):
    url = 'https://api.hh.ru/vacancies'

    json = requests.get(url, params=get_query_parameters(title, area, 0)).json()

    vacancies = json["items"]
    print("0 req")
    for i in range(1, 5):#min(200, json["pages"] + 1)):
        r = requests.get(url, params=get_query_parameters(title, area, i))
        json = r.json()
        vacancies.extend(json["items"])
        print(f"{i} req")

    return vacancies


def get_vacancies_by_country(title):
    url = 'https://api.hh.ru/vacancies'

    vacancies = []

    return vacancies


# ans = get_vacancies("flutter")
# a = 1
# for title in vacancy_titles:
#     with open(file_name, "w", encoding="utf-8") as json_file:
#         json.dump(data, json_file, ensure_ascii=False, indent=4)
#
# print(f"Данные успешно сохранены в файл {file_name}")

# Регионы
areas_url = "https://api.hh.ru/areas"
areas = requests.get(areas_url).json()
areas_ids = [area['id'] for area in areas[0]['areas']]  # id регионов рф

with open("first_data2.json", "w", encoding="utf-8") as json_file:
    # for area in areas_ids:
    area = 113
    for vac_title, vac_promt in VACANCY_TITLES.items():
        print("processing  " + vac_title)
        ans = get_1_vacancy(vac_promt, area)
        json.dump(ans, json_file, ensure_ascii=False, indent=4)
        print('done\n')
        # break
    print(area)
print(f"Данные успешно сохранены в файл first_data2.json")
