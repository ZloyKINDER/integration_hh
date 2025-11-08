from src.utils.utils import filter_vacancies, get_by_salary, get_top, sort_vacancies
from src.vacancy.vacancy import Vacancy


def test_filter():
    vs = [Vacancy("A", "url", None, "key"), Vacancy("B", "url", None, "no")]
    assert len(filter_vacancies(vs, ["key"])) == 1


def test_salary():
    vs = [Vacancy("A", "url", {"from": 100, "to": 150}, ""), Vacancy("B", "url", {"from": 200}, "")]
    assert len(get_by_salary(vs, "100-150")) == 1


def test_sort():
    vs = [Vacancy("A", "url", {"from": 100}, ""), Vacancy("B", "url", {"from": 200}, "")]
    assert sort_vacancies(vs)[0].salary_from == 200


def test_top():
    vs = [Vacancy("A", "url", None, ""), Vacancy("B", "url", None, "")]
    assert len(get_top(vs, 1)) == 1
