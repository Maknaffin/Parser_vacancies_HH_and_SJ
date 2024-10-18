import os

import requests

from src.abstract_classes import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_query):
        """Получение вакансий через API HeadHunter"""

        url = f'{self.url}/?text={search_query}&per_page=100'
        response = requests.get(url)

        if response.status_code == 200:
            # получение вакансий
            vacancies = response.json()['items']
            return vacancies
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')

    def validations_vacancies(self, hh_vacancies_list):
        """Валидация данных из списка вакансий HeadHunter"""

        filter_vac_list = []
        for vacancy in hh_vacancies_list:
            if vacancy["salary"] is not None:
                if vacancy["salary"]["currency"] == "RUR":
                    salary_currency = vacancy["salary"]["currency"]
                else:
                    salary_currency = False

                if vacancy["salary"]["from"]:
                    salary_from = vacancy["salary"]["from"]
                else:
                    salary_from = False

                if vacancy["salary"]["to"]:
                    salary_to = vacancy["salary"]["to"]
                else:
                    salary_to = False
            else:
                salary_currency = salary_from = salary_to = False

            if salary_currency and salary_from and salary_to:
                filter_vac_list.append(vacancy)
        return filter_vac_list

    def data_formatting(self, hh_val_vacancies):
        """Форматирование вакансий HeadHunter по общим ключам"""

        format_vac_list = []
        for data in hh_val_vacancies:
            format_data = {
                "Наименование вакансии": data["name"],
                "Ссылка на вакансию": data["alternate_url"],
                "Зарплата от": data["salary"]["from"],
                "Зарплата до": data["salary"]["to"],
                "Валюта": data["salary"]["currency"],
                "Название компании": data["employer"]["name"],
                "Требования и обязанности": data["snippet"]["requirement"],
                "Регион": data["area"]["name"]
            }
            format_vac_list.append(format_data)
        return format_vac_list


class SuperJobAPI(VacancyAPI):
    """Класс для работы с API SuperJob"""

    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.headers = {'X-Api-App-Id': os.getenv('SJ_API_KEY')}

    def get_vacancies(self, search_query):
        """Получение вакансий через API SuperJob"""

        url = f'{self.url}/?keyword={search_query}'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            # получение вакансий
            vacancies = response.json()['objects']
            return vacancies
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')

    def validations_vacancies(self, sj_vacancies_list):
        """Валидация данных из списка вакансий SuperJob"""

        filter_vac_list = []
        for vacancy in sj_vacancies_list:
            if vacancy["payment_from"] is not None:
                if vacancy["payment_from"]:
                    payment_from = vacancy["payment_from"]
                else:
                    payment_from = False

                if vacancy["payment_to"]:
                    payment_to = vacancy["payment_to"]
                else:
                    payment_to = False

                if vacancy["currency"] == "rub":
                    currency = vacancy["currency"]
                else:
                    currency = False

            else:
                currency = payment_from = payment_to = False

            if currency and payment_from and payment_to:
                filter_vac_list.append(vacancy)

        return filter_vac_list

    def data_formatting(self, sj_val_vacancies):
        """Форматирование вакансий SuperJob по общим ключам"""

        format_vac_list = []
        for data in sj_val_vacancies:
            format_data = {
                "Наименование вакансии": data["profession"],
                "Ссылка на вакансию": data["link"],
                "Зарплата от": data["payment_from"],
                "Зарплата до": data["payment_to"],
                "Валюта": data["currency"],
                "Название компании": data["firm_name"],
                "Требования и обязанности": data["candidat"],
                "Регион": data["town"]["title"]
            }
            format_vac_list.append(format_data)
        return format_vac_list
