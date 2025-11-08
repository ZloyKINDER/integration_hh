from typing import List

from ..vacancy.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], words: List[str]) -> List[Vacancy]:
    """Фильтрация по ключевым словам."""
    if not words:
        return vacancies
    return [v for v in vacancies if any(w.lower() in v.description.lower() for w in words)]


def get_by_salary(vacancies: List[Vacancy], range_str: str) -> List[Vacancy]:
    """Фильтрация по зарплате (формат 'min-max')."""
    if not range_str:
        return vacancies
    try:
        min_s, max_s = map(int, range_str.split("-"))
        filtered = []
        for v in vacancies:
            # Используем salary_from как минимальную зарплату, salary_to как максимальную
            # Если salary_to не указано, считаем что зарплата фиксированная (salary_from)
            salary_min = v.salary_from
            salary_max = v.salary_to if v.salary_to > 0 else v.salary_from
            # Проверяем пересечение диапазонов
            if salary_min <= max_s and salary_max >= min_s:
                filtered.append(v)
        return filtered
    except (ValueError, AttributeError):
        return vacancies


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка по убыванию зарплаты."""
    return sorted(vacancies, reverse=True)


def get_top(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """Топ N."""
    return vacancies[:n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Читаемый вывод."""
    for v in vacancies:
        print(v)
        print("-" * 80)
