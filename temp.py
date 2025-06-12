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
