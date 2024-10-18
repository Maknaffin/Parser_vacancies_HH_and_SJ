import json

from src.func_user import filtered_vacancies, sorted_vacancies, top_vacancies, print_vacancies
from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from src.vacancy_api import HeadHunterAPI, SuperJobAPI

if __name__ == "__main__":
    search_query = input("Введите поисковый запрос: ").capitalize()

    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()

    # Получение списка вакансий по API
    hh_vacancies_list = hh_api.get_vacancies(search_query)
    sj_vacancies_list = sj_api.get_vacancies(search_query)

    # Валидация полученных вакансий
    hh_val_vacancies = hh_api.validations_vacancies(hh_vacancies_list)
    sj_val_vacancies = sj_api.validations_vacancies(sj_vacancies_list)

    # приведение к общим ключам вакансий с платформ
    vacancies_hh = hh_api.data_formatting(hh_val_vacancies)
    vacancies_sj = sj_api.data_formatting(sj_val_vacancies)

    # добавление вакансий в файл
    js_saver = JSONSaver()
    js_saver.add_vacancies(vacancies_hh)
    js_saver.add_vacancies(vacancies_sj)

    # получение вакансий из файла
    list_vacancies = js_saver.get_vacancies()

    # создание списка экземпляров класса вакансий
    lst_inst_vacancies = [Vacancy(
        vacancy["Наименование вакансии"], vacancy["Ссылка на вакансию"],
        vacancy["Зарплата от"], vacancy["Зарплата до"],
        vacancy["Требования и обязанности"], vacancy["Регион"])
        for vacancy in list_vacancies]

    # взаимодействие с пользователем
    top_num = int(input('Введите количество вакансий для вывода в топ: '))
    filter_area = input('Введите название города для поиска вакансии: ').title()
    filter_vacancies = filtered_vacancies(lst_inst_vacancies, filter_area)

    if not filter_vacancies:
        print("Нет вакансий, соответствующих заданным критериям")

    sort_vacancies = sorted_vacancies(filter_vacancies)
    top_vacancy = top_vacancies(sort_vacancies, top_num)
    printing = print_vacancies(top_vacancy)
