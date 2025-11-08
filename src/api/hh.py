from typing import Dict, List

import requests

from src.api.abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """Класс для интеграции с API HH.ru (наследует AbstractAPI)."""

    def __init__(self) -> None:
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-Vacancies-App/1.0"}

    def __private_connect(self) -> None:
        """Приватный метод проверки подключения (запрос к словарям)."""
        try:
            response = requests.get("https://api.hh.ru/dictionaries", headers=self.__headers)
            if response.status_code != 200:
                raise ConnectionError(f"HH API unavailable: status {response.status_code}")
        except requests.RequestException as e:
            raise ConnectionError(f"Connection error: {str(e)}")

    def connect(self) -> None:
        """Публичный метод подключения."""
        self.__private_connect()

    def get_vacancies(self, keyword: str, per_page: int = 100) -> List[Dict]:
        """Получение вакансий с проверкой подключения."""
        self.connect()
        params = {"text": keyword, "area": 113, "per_page": per_page, "only_with_salary": True}  # Россия
        response = requests.get(self.__base_url, params=params, headers=self.__headers)
        if response.status_code != 200:
            raise ValueError(f"Request failed: {response.status_code}")
        return response.json()["items"]