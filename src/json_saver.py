import json
from src.abstract_classes import FileSaver


class JSONSaver(FileSaver):
    """Класс для работы с файлами json"""

    def __init__(self):
        self.list_vacancies = []

        try:
            with open('../data/vacancies.json', 'r', encoding='utf-8') as file:
                self.list_vacancies = json.load(file)
        except FileNotFoundError:
            print('Неверный путь к файлу')
        except json.decoder.JSONDecodeError:
            pass

    def add_vacancies(self, list_vacancies):
        """Метод для добавления вакансий в файл"""

        for vacancy in list_vacancies:
            if vacancy not in self.list_vacancies:
                self.list_vacancies.append(vacancy)

        with open('../data/vacancies.json', 'w', encoding='UTF-8') as file:
            json.dump(self.list_vacancies, file, indent=2, ensure_ascii=False)

    def get_vacancies(self):
        """Метод для получения вакансий из файла"""

        with open('../data/vacancies.json', 'r', encoding='UTF-8') as file:
            return json.load(file)
