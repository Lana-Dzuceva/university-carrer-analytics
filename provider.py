import requests


def get_vacancies(title):
    url = 'https://api.hh.ru/vacancies'
    vacancies = []
    par = {'text': title, 'area': '113', 'per_page': '10', 'page': 0}
    r = requests.get(url, params=par)
    json = r.json()
    vacancies.append(json["items"])
    for i in range(min(200)):
        # параметры, которые будут добавлены к запросу
        par = {'text': title, 'area': '113', 'per_page': '10', 'page': i}
        r = requests.get(url, params=par)
        json = r.json()
        vacancies.append(json["items"])
    return vacancies


get_vacancies("flutter")