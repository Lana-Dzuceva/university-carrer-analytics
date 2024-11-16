def get_vacancies(title):
    for i in range(10):
        # запрос
        url = 'https://api.hh.ru/vacancies'
        # параметры, которые будут добавлены к запросу
        par = {'text': 'flutter', 'area': '113', 'per_page': '10', 'page': i}
        r = requests.get(url, params=par)
        e = r.json()
        x.append(e)