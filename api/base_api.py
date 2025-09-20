# Импорт необходимых библиотек
import allure  # Библиотека для создания отчетов Allure
import requests  # Библиотека для отправки HTTP-запросов


# Базовый класс для всех API клиентов
class BaseApi:
    # Конструктор класса, инициализирует базовый URL API
    def __init__(self):
        # Установка базового URL для всех запросов
        self.base_url = "https://qa-scooter.praktikum-services.ru/api/v1"

    # Метод для выполнения GET запросов с добавлением шага в Allure отчет
    @allure.step("GET запрос к {path}")  # Декоратор для добавления шага в отчет
    def get(self, path, **kwargs):
        # Выполнение GET запроса и возврат ответа
        return requests.get(f"{self.base_url}{path}", **kwargs)

    # Метод для выполнения POST запросов с добавлением шага в Allure отчет
    @allure.step("POST запрос к {path}")  # Декоратор для добавления шага в отчет
    def post(self, path, **kwargs):
        # Выполнение POST запроса и возврат ответа
        return requests.post(f"{self.base_url}{path}", **kwargs)

    # Метод для выполнения DELETE запросов с добавлением шага в Allure отчет
    @allure.step("DELETE запрос к {path}")  # Декоратор для добавления шага в отчет
    def delete(self, path, **kwargs):
        # Выполнение DELETE запроса и возврат ответа
        return requests.delete(f"{self.base_url}{path}", **kwargs)

    # Метод для выполнения PUT запросов с добавлением шага в Allure отчет
    @allure.step("PUT запрос к {path}")  # Декоратор для добавления шага в отчет
    def put(self, path, **kwargs):
        # Выполнение PUT запроса и возврат ответа
        return requests.put(f"{self.base_url}{path}", **kwargs)