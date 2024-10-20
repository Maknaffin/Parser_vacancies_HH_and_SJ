from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Абстрактный метод для получения вакансий"""
        pass
