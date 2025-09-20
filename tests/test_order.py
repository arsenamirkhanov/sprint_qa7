# Импорт необходимых библиотек и модулей
import pytest  # Фреймворк для тестирования
import allure  # Библиотека для создания отчетов Allure
from api.order_api import OrderApi  # API для работы с заказами
from utilities.generate_data import generate_order_data  # Функции для генерации тестовых данных


# Класс для тестирования функциональности заказов
@allure.epic("API тесты сервиса QA Scooter")  # Эпик для группировки тестов в отчете
@allure.feature("Тесты заказов")  # Фича для группировки тестов в отчете
class TestOrder:
    # Фикстура, которая выполняется перед каждым тестом
    @pytest.fixture(autouse=True)
    def setup(self):
        # Создание экземпляра API для работы с заказами
        self.api = OrderApi()

    # Тест создания заказа с разными цветами
    @allure.story("Создание заказа")  # История для группировки тестов в отчете
    @allure.title("Создание заказа с разными цветами")  # Заголовок теста в отчете
    @pytest.mark.parametrize("color", [  # Параметризация теста с разными цветами
        ["BLACK"],  # Тест с черным цветом
        ["GREY"],  # Тест с серым цветом
        ["BLACK", "GREY"],  # Тест с обоими цветами
        []  # Тест без указания цвета
    ])
    def test_create_order_with_different_colors(self, color):
        # Шаг подготовки данных заказа
        with allure.step("Подготовка данных заказа"):
            # Генерация данных заказа с указанным цветом
            order_data = generate_order_data(color)

        # Шаг создания заказа
        with allure.step("Создание заказа"):
            # Отправка запроса на создание заказа
            response = self.api.create_order(order_data)

        # Шаг проверки ответа
        with allure.step("Проверка ответа"):
            # Проверка статус кода ответа
            assert response.status_code == 201
            # Проверка наличия номера трека в ответе
            assert "track" in response.json()

    # Тест получения списка заказов
    @allure.story("Список заказов")  # История для группировки тестов в отчете
    @allure.title("Получение списка заказов")  # Заголовок теста в отчете
    def test_get_orders_list(self):
        # Шаг запроса списка заказов
        with allure.step("Запрос списка заказов"):
            # Отправка запроса на получение списка заказов
            response = self.api.get_orders_list()

        # Шаг проверки ответа
        with allure.step("Проверка ответа"):
            # Проверка статус кода ответа
            assert response.status_code == 200
            # Проверка наличия ключа "orders" в ответе
            assert "orders" in response.json()
            # Проверка, что значение ключа "orders" является списком
            assert isinstance(response.json()["orders"], list)