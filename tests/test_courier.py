# Импорт необходимых библиотек и модулей
import pytest  # Фреймворк для тестирования
import allure  # Библиотека для создания отчетов Allure
from api.courier_api import CourierApi  # API для работы с курьерами
from utilities.generate_data import generate_courier_data
from utilities.generate_data import register_new_courier

# Класс для тестирования функциональности курьеров
@allure.epic("API тесты сервиса QA Scooter")  # Эпик для группировки тестов в отчете
@allure.feature("Тесты курьера")  # Фича для группировки тестов в отчете
class TestCourier:
    # Фикстура, которая выполняется перед каждым тестом
    @pytest.fixture(autouse=True)
    def setup(self):
        # Создание экземпляра API для работы с курьерами
        self.api = CourierApi()

    # Тест успешного создания курьера
    @allure.story("Создание курьера")  # История для группировки тестов в отчете
    @allure.title("Успешное создание курьера")  # Заголовок теста в отчете
    def test_create_courier_success(self, cleanup_courier):
        # Шаг подготовки тестовых данных
        with allure.step("Подготовка тестовых данных"):
            # Генерация данных для курьера
            courier_data = generate_courier_data()

        # Шаг создания курьера
        with allure.step("Создание курьера"):
            # Отправка запроса на создание курьера
            response = self.api.create_courier(courier_data)

        # Шаг проверки ответа
        with allure.step("Проверка ответа"):
            # Проверка статус кода ответа
            assert response.status_code == 201
            # Проверка тела ответа
            assert response.json() == {"ok": True}

        # Получаем ID курьера для очистки
        login_response = self.api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            cleanup_courier = login_response.json()["id"]

    # Тест создания дубликата курьера
    @allure.story("Создание курьера")  # История для группировки тестов в отчете
    @allure.title("Создание дубликата курьера")  # Заголовок теста в отчете
    def test_create_duplicate_courier(self, cleanup_courier):
        # Шаг регистрации курьера
        with allure.step("Регистрация курьера"):
            # Регистрация нового курьера
            courier_data = register_new_courier()
            assert courier_data is not None, "Не удалось зарегистрировать курьера"

        # Шаг попытки создания дубликата
        with allure.step("Попытка создания дубликата"):
            # Отправка запроса на создание курьера с теми же данными
            response = self.api.create_courier(courier_data)

        # Шаг проверки ошибки
        with allure.step("Проверка ошибки"):
            # Проверка статус кода ответа (конфликт)
            assert response.status_code == 409

        # Получаем ID курьера для очистки
        login_response = self.api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            cleanup_courier = login_response.json()["id"]

    # Тест создания курьера без обязательного поля
    @allure.story("Создание курьера")  # История для группировки тестов в отчете
    @allure.title("Создание курьера без обязательного поля")  # Заголовок теста в отчете
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])  # Параметризация теста
    def test_create_courier_missing_required_field(self, missing_field):
        # Шаг подготовки данных с отсутствующим полем
        with allure.step("Подготовка данных с отсутствующим полем"):
            # Генерация данных для курьера
            courier_data = generate_courier_data()
            # Удаление обязательного поля
            del courier_data[missing_field]

        # Шаг создания курьера с неполными данными
        with allure.step("Создание курьера с неполными данными"):
            # Отправка запроса на создание курьера
            response = self.api.create_courier(courier_data)

        # Шаг проверки ошибки
        with allure.step("Проверка ошибки"):
            # Проверка статус кода ответа (неверный запрос)
            assert response.status_code == 400

    # Тест успешного логина курьера
    @allure.story("Логин курьера")  # История для группировки тестов в отчете
    @allure.title("Успешный логин курьера")  # Заголовок теста в отчете
    def test_login_courier_success(self, cleanup_courier):
        # Шаг регистрации курьера
        with allure.step("Регистрация курьера"):
            # Регистрация нового курьера
            courier_data = register_new_courier()
            assert courier_data is not None, "Не удалось зарегистрировать курьера"

        # Шаг логина курьера
        with allure.step("Логин курьера"):
            # Создание учетных данных для авторизации
            credentials = {
                "login": courier_data["login"],
                "password": courier_data["password"]
            }
            # Отправка запроса на авторизацию курьера
            response = self.api.login_courier(credentials)

        # Шаг проверки ответа
        with allure.step("Проверка ответа"):
            # Проверка статус кода ответа
            assert response.status_code == 200
            # Проверка наличия ID в ответе
            assert "id" in response.json()

            # Сохраняем ID для очистки
            cleanup_courier = response.json()["id"]

    # Тест логина с неверным паролем
    @allure.story("Логин курьера")  # История для группировки тестов в отчете
    @allure.title("Логин с неверным паролем")  # Заголовок теста в отчете
    def test_login_with_wrong_password(self, cleanup_courier):
        # Шаг регистрации курьера
        with allure.step("Регистрация курьера"):
            # Регистрация нового курьера
            courier_data = register_new_courier()
            assert courier_data is not None, "Не удалось зарегистрировать курьера"

        # Шаг логина с неверным паролем
        with allure.step("Логин с неверным паролем"):
            # Создание учетных данных с неверным паролем
            credentials = {
                "login": courier_data["login"],
                "password": "wrong_password"
            }
            # Отправка запроса на авторизацию курьера
            response = self.api.login_courier(credentials)

        # Шаг проверки ошибки
        with allure.step("Проверка ошибки"):
            # Проверка статус кода ответа (не найдено)
            assert response.status_code == 404

        # Получаем ID курьера для очистки
        login_response = self.api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            cleanup_courier = login_response.json()["id"]

    # Тест логина без пароля
    @allure.story("Логин курьера")  # История для группировки тестов в отчете
    @allure.title("Логин без пароля")  # Заголовок теста в отчете
    def test_login_without_password(self, cleanup_courier):
        # Шаг регистрации курьера
        with allure.step("Регистрация курьера"):
            # Регистрация нового курьера
            courier_data = register_new_courier()
            assert courier_data is not None, "Не удалось зарегистрировать курьера"

        # Шаг логина без пароля
        with allure.step("Логин без пароля"):
            # Создание учетных данных без пароля
            credentials = {"login": courier_data["login"]}
            # Отправка запроса на авторизацию курьера
            response = self.api.login_courier(credentials)

        # Шаг проверки ошибки
        with allure.step("Проверка ошибки"):
            # Проверка статус кода ответа (неверный запрос)
            assert response.status_code == 400

        # Получаем ID курьера для очистки
        login_response = self.api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            cleanup_courier = login_response.json()["id"]

    # Тест логина несуществующего курьера
    @allure.story("Логин курьера")  # История для группировки тестов в отчете
    @allure.title("Логин несуществующего курьера")  # Заголовок теста в отчете
    def test_login_nonexistent_courier(self):
        # Шаг логина с случайными данными
        with allure.step("Логин с случайными данными"):
            # Создание случайных учетных данных
            credentials = {
                "login": "nonexistent",
                "password": "invalid"
            }
            # Отправка запроса на авторизацию курьера
            response = self.api.login_courier(credentials)

        # Шаг проверки ошибки
        with allure.step("Проверка ошибки"):
            # Проверка статус кода ответа (не найдено)
            assert response.status_code == 404