# Импорт необходимых библиотек и модулей
import allure  # Библиотека для создания отчетов Allure
from api.base_api import BaseApi  # Базовый класс API


# Класс для работы с API курьеров, наследуется от BaseApi
class CourierApi(BaseApi):
    # Конструктор класса, вызывает конструктор родительского класса
    def __init__(self):
        # Вызов конструктора родительского класса BaseApi
        super().__init__()

    # Метод для создания курьера с добавлением шага в Allure отчет
    @allure.step("Создание курьера")  # Декоратор для добавления шага в отчет
    def create_courier(self, data):
        # Выполнение POST запроса для создания курьера
        return self.post("/courier", data=data)

    # Метод для авторизации курьера с добавлением шага в Allure отчет
    @allure.step("Логин курьера")  # Декоратор для добавления шага в отчет
    def login_courier(self, credentials):
        # Выполнение POST запроса для авторизации курьера
        return self.post("/courier/login", data=credentials)

    # Метод для удаления курьера с добавлением шага в Allure отчет
    @allure.step("Удаление курьера {courier_id}")  # Декоратор для добавления шага в отчет
    def delete_courier(self, courier_id):
        # Выполнение DELETE запроса для удаления курьера
        return self.delete(f"/courier/{courier_id}")