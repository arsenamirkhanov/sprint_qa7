# Импорт необходимых библиотек и модулей
import allure  # Библиотека для создания отчетов Allure
from api.base_api import BaseApi  # Базовый класс API


# Класс для работы с API заказов, наследуется от BaseApi
class OrderApi(BaseApi):
    # Конструктор класса, вызывает конструктор родительского класса
    def __init__(self):
        # Вызов конструктора родительского класса BaseApi
        super().__init__()

    # Метод для создания заказа с добавлением шага в Allure отчет
    @allure.step("Создание заказа")  # Декоратор для добавления шага в отчет
    def create_order(self, order_data):
        # Выполнение POST запроса для создания заказа с данными в формате JSON
        return self.post("/orders", json=order_data)

    # Метод для получения списка заказов с добавлением шага в Allure отчет
    @allure.step("Получение списка заказов")  # Декоратор для добавления шага в отчет
    def get_orders_list(self):
        # Выполнение GET запроса для получения списка заказов
        return self.get("/orders")