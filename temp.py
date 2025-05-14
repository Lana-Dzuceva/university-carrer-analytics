import json
import requests

# парсю все регионы с hh.ru
with open("areas.json", "w", encoding="utf-8") as json_file:
    areas_url = "https://api.hh.ru/areas"
    areas = requests.get(areas_url).json()
    areas_ids = [(area['id'], area['name']) for area in areas[0]['areas']]  # id регионов рф
    json.dump(areas_ids, json_file, ensure_ascii=False, indent=4)
    area = 113
    print(f"Данные успешно сохранены в файл areas.json")
