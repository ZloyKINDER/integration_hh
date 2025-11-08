from abc import ABC, abstractmethod
from typing import Dict, List


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API вакансий (наследуется для конкретных платформ)."""

    @abstractmethod
    def connect(self) -> None:
        """Подключение к API с проверкой доступности."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 100) -> List[Dict]:
        """Получение списка вакансий по ключевому слову."""
        pass
