from src.vacancy.vacancy import Vacancy


def test_init():
    v = Vacancy("Test", "url", {"from": 100}, "desc")
    assert v.salary_from == 100


def test_validate():
    v = Vacancy("Test", "url", None, "desc")
    assert v.salary_from == 0


def test_compare():
    v1 = Vacancy("A", "url", {"from": 100}, "desc")
    v2 = Vacancy("B", "url", {"from": 200}, "desc")
    assert v1 < v2


def test_cast():
    data = [
        {
            "name": "Test",
            "alternate_url": "url",
            "salary": {"from": 100},
            "snippet": {"requirement": "", "responsibility": ""},
            "employer": {"name": ""},
        }
    ]
    vs = Vacancy.cast_to_object_list(data)
    assert len(vs) == 1
