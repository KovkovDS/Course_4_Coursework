# Импортируем модуль abc для использования абстрактных классов
from abc import ABC, abstractmethod


class VacanciesAPI(ABC):
    """Абстрактный класс для работы c API сервисов с вакансиями."""

    def __init__(self):
        """Инициирует конструктор класса."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, pages_count: int) -> list:
        """Получает ответ на get-запрос и записывает его в список вакансий при подключении к API сервиса с
        вакансиями."""
        pass
