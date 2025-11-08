from typing import Dict, List, Optional


class Vacancy:
    """Класс вакансии с валидацией и сравнением по зарплате (инкапсуляция)."""

    __slots__ = ("name", "url", "salary_from", "salary_to", "description", "employer")

    def __init__(self, name: str, url: str, salary: Optional[Dict], description: str, employer: str = "") -> None:
        self.name = name
        self.url = url
        self.salary_from = self.__validate_salary(salary.get("from") if salary else None)
        self.salary_to = self.__validate_salary(salary.get("to") if salary else None)
        self.description = description
        self.employer = employer

    def __validate_salary(self, value: Optional[int]) -> int:
        """Приватная валидация зарплаты (0 если не указана)."""
        return value if isinstance(value, (int, float)) and value > 0 else 0

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary_from < other.salary_from

    def __le__(self, other: "Vacancy") -> bool:
        return self.salary_from <= other.salary_from

    def __eq__(self, other: "Vacancy") -> bool:
        return self.salary_from == other.salary_from

    def __str__(self) -> str:
        salary = f"{self.salary_from}-{self.salary_to}" if self.salary_to else str(self.salary_from)
        salary = salary if salary != "0" else "Не указана"
        return (
            f"{self.name} ({self.employer}) | Зарплата: {salary} | {self.url}\nОписание: {self.description[:100]}..."
        )

    @classmethod
    def cast_to_object_list(cls, data: List[Dict]) -> List["Vacancy"]:
        """Конвертация JSON в список Vacancy."""
        vacancies = []
        for v in data:
            # Исправление: проверка на None и замена на пустую строку
            requirement = v["snippet"].get("requirement") or ""
            responsibility = v["snippet"].get("responsibility") or ""
            description = requirement + responsibility

            vacancies.append(
                cls(
                    v["name"],
                    v["alternate_url"],
                    v.get("salary"),
                    description,
                    v["employer"]["name"],
                )
            )
        return vacancies
