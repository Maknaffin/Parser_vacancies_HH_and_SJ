class Vacancy:
    """Класс для работы с вакансиями"""
    # __slots__ = ('__title', '__link', '__salary_from', '__salary_to', '__requirements', '__town')

    def __init__(self, title, link, salary_from, salary_to, requirements, town):
        self.title = title
        self.link = link
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirements = requirements
        self.town = town

    def __lt__(self, other) -> bool:
        """Сравнение вакансий по зарплате если объект 1 < 2"""

        return self.salary < other.salary

    def __gt__(self, other) -> bool:
        """Сравнение вакансий по зарплате если объект 1 > 2"""

        return self.salary > other.salary