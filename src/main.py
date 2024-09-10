import json

from src.vacancy_api import HeadHunterAPI, SuperJobAPI

if __name__ == "__main__":
    search_query = input("Введите поисковый запрос: ").capitalize()

    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()

    # Получение списка вакансий по API
    hh_vacancies_list = hh_api.get_vacancies(search_query)
    sj_vacancies = sj_api.get_vacancies(search_query)

    # Валидация полученных вакансий
    hh_val_vacancies = hh_api.hh_validations_vacancies(hh_vacancies_list)
    sj_val_vacancies = sj_api.sj_validations_vacancies(sj_vacancies)

    # приведение к общим ключам вакансий с платформ
    vacancies_hh = hh_api.hh_data_formatting(hh_val_vacancies)
    vacancies_sj = sj_api.sj_data_formatting(sj_val_vacancies)


    # print(json.dumps(vacancies_sj, indent=2, ensure_ascii=False))

