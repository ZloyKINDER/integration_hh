from src.api.hh import HeadHunterAPI
from src.storage.json_storage import JSONSaver
from src.utils.utils import filter_vacancies, get_by_salary, get_top, print_vacancies, sort_vacancies
from src.vacancy.vacancy import Vacancy


def user_interaction():
    api = HeadHunterAPI()
    saver = JSONSaver()
    query = input("Поисковый запрос: ")
    vacancies_data = api.get_vacancies(query)
    # API возвращает список вакансий напрямую
    if isinstance(vacancies_data, list) and len(vacancies_data) > 0:
        # Сохраняем каждую вакансию отдельно
        for vacancy in vacancies_data:
            saver.add_vacancy(vacancy)
        # Создаем объекты Vacancy из списка вакансий
        vacancies = Vacancy.cast_to_object_list(vacancies_data)
    else:
        print("Нет данных от API")
        return
    # Обработка ввода Top N с проверкой
    while True:
        n_input = input("Топ N: ").strip()
        if n_input and n_input.isdigit():
            n = int(n_input)
            break
        else:
            print("Пожалуйста, введите число")
    words = input("Ключевые слова (пробел): ").split()
    range_str = input("Диапазон зарплат (min-max): ")
    filtered = filter_vacancies(vacancies, words)
    ranged = get_by_salary(filtered, range_str)
    sorted_v = sort_vacancies(ranged)
    top = get_top(sorted_v, n)
    print_vacancies(top)
    # Удаляем первую вакансию для демонстрации
    if vacancies_data and len(vacancies_data) > 0:
        saver.delete_vacancy(vacancies_data[0])
        print("Удалена первая вакансия.")


if __name__ == "__main__":
    user_interaction()