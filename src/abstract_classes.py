from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, search_query):
        """Абстрактный метод для получения вакансий"""
        pass

    @abstractmethod
    def validations_vacancies(self, vacancies_list):
        """Абстрактный метод для валидации данных из списка вакансий"""
        pass

    @abstractmethod
    def data_formatting(self, val_vacancies):
        """Абстрактный метод для форматирования данных из вакансий по общим ключам"""
        pass


class FileSaver(ABC):
   """Абстрактный класс для работы с файлами json"""

   @abstractmethod
   def add_vacancies(self, vacancies_list):
       """Абстрактный метод для добавления вакансий в файл"""
       pass

   @abstractmethod
   def get_vacancies(self):
       """Абстрактный метод для получения вакансий из файла"""
       pass