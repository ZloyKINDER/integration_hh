import json
import os
from typing import Any, Dict, List, Optional

from .abstract_storage import AbstractStorage


class JSONSaver(AbstractStorage):
    """JSON-коннектор (наследует AbstractStorage)."""

    def __init__(self, file_name: str = "data/vacancies.json") -> None:
        self.__file_name = file_name

    def __load(self) -> List[Dict]:
        if os.path.exists(self.__file_name):
            with open(self.__file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Если данные в формате {"items": [...]}, возвращаем список вакансий
                if isinstance(data, dict) and "items" in data:
                    return data["items"]
                return data
        return []

    def __save(self, data: List[Dict]) -> None:
        # Создаем директорию, если её нет
        os.makedirs(os.path.dirname(self.__file_name), exist_ok=True)
        with open(self.__file_name, "w", encoding="utf-8") as f:
            # Сохраняем в формате {"items": [...]} для совместимости
            json.dump({"items": data}, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Dict) -> None:
        data = self.__load()
        if not any(v["id"] == vacancy["id"] for v in data):  # Нет дубликатов по ID
            data.append(vacancy)
        self.__save(data)

    def get_vacancies(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict]:
        data = self.__load()
        if criteria:
            return [v for v in data if all(v.get(k) == criteria[k] for k in criteria)]
        return data

    def delete_vacancy(self, vacancy: Dict) -> None:
        data = self.__load()
        data = [v for v in data if v["id"] != vacancy["id"]]
        self.__save(data)

    # Заглушки для других
    def add_to_csv(self, vacancy: Dict) -> None:
        raise NotImplementedError("CSV not implemented")
