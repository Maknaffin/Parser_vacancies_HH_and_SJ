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