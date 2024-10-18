def filtered_vacancies(lst_inst_vacancies, filter_area):
    """Фильтрация вакансий по городу"""

    res = []
    for inst_vacancy in lst_inst_vacancies:
        if filter_area == inst_vacancy.town:
            res.append(inst_vacancy)

    return res


def sorted_vacancies(filter_vacancies):
    """Сортировка вакансий по минимальной зарплате"""
    lst = [(item, item.salary_from) for item in filter_vacancies]
    sort_list = sorted(lst, key=lambda x: x[1], reverse=True)
    res = [item[0] for item in sort_list]

    return res


def top_vacancies(sort_vacancies, top_num):
    """Вывод топ N вакансий"""

    return sort_vacancies[:top_num]


def print_vacancies(res):
    """Вывод вакансий в удобном для пользователя виде"""

    for i, v in enumerate(res):
        print(f"{i + 1}. Наименование вакансии: {v.title},\n"
              f"   Ссылка на вакансию: {v.link}\n"
              f"   Зарплата от {v.salary_from}\n"
              f"   Зарплата до {v.salary_to},\n"
              f"   Требования и обязанности: {v.requirements},\n"
              f"   Регион: {v.town}")
