from src.vacancy_api import HeadHunterAPI, SuperJobAPI

if __name__ == "__main__":
    search_query = input("Введите поисковый запрос: ").capitalize()

    # Поиск вакансий по запросу с API
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    sj_vacancies = sj_api.get_vacancies(search_query)


