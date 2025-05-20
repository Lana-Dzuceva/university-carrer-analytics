import json

import duckdb
import requests
from db_connection import *
from constants import PROFESSIONAL_ROLES, VACANCY_TITLES
from utils import safe_get

class Parser:
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        pass

    def parse_all_data(self):
        """
        Запустить парсер, который пройдется по всем регионам из файла Russia_regions.json
        """
        try:
            with open("text_files/Russia_regions.json", "r", encoding="utf-8") as file:
                regions = json.load(file)

                result = self.get_vacancies_by_regions(regions)
                # print(len(result))
                # insert_all_vacancies(result)
                insert_vacancies2(result)

        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле Russia_regions.json.")
            return []
        except duckdb.IOException as e:
            print(e)
        except Exception as e:
            print(e)

    def get_vacancies_by_regions(self, regions):
        result = []
        for short_title, title_for_request in VACANCY_TITLES.items():
            for region in regions:  # todo: remove [:5]
                # region = [
                #     "1679",
                #     "Нижегородская область"
                # ],
                region_id, region_name = region
                result += self.get_vacancies_by_title(title_for_request, short_title, area=region_id)
        return result

    def get_vacancies_by_title(self, title_for_request, short_title, area=113):
        title_for_request = title_for_request.lstrip("\"\n ")
        response_json = requests.get(self.BASE_URL, params=self.get_query_parameters(title_for_request, area, 0)).json()
        vacancies = safe_get(response_json, "items", [])
        vacancies = [self.get_detailed_vac(res) for res in vacancies]

        print("{0} {1} pages: {2} found: {3}".format(short_title, str(area), str(response_json.get("pages", '0')),
                                                     str(response_json.get("found", '0'))))
        for i in range(1, min(100, int(response_json.get("pages", '0')) + 1)):# min(2, int(response_json.get("pages", '0')))):  # min(200, json["pages"] + 1)):
            try:
                r = requests.get(self.BASE_URL, params=self.get_query_parameters(title_for_request, area, i))
                response_json = r.json()
                result = safe_get(response_json, "items", [])
                result = [self.get_detailed_vac(res) for res in result]
                vacancies.extend(result)
            except Exception as e:
                print(e)
        for vac in vacancies:
            vac["group_tag "] = short_title

        return vacancies

    def get_detailed_vac(self, item):
        try:
            url = item['url']
            response = requests.get(url)

            if response.status_code == 200:
                vacancy_details = response.json()
                return vacancy_details
        except Exception as e:
            print(e)

    @staticmethod
    def get_query_parameters(title, area, page):
        par2 = [('text', title), ('area', area), ('per_page', '20'), ('page', page)]
        # par2.extend(PROFESSIONAL_ROLES)  # TODO вернуть эту строку
        return par2
