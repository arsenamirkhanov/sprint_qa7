# Импорт необходимых библиотек
import pytest  # Фреймворк для тестирования
import allure  # Библиотека для создания отчетов Allure
from api.courier_api import CourierApi  # API для работы с курьерами


# Фикстура для очистки данных после выполнения тестов
@pytest.fixture
def cleanup_courier():
    courier_id = None  # Инициализация переменной для хранения ID курьера
    yield courier_id  # Возврат управления тесту

    # Очистка после выполнения теста
    if courier_id:  # Если ID курьера был установлен
        with allure.step("Удаление тестового курьера"):  # Шаг в отчете Allure
            response = CourierApi().delete_courier(courier_id)  # Удаление курьера
            # Проверяем успешность удаления
            assert response.status_code == 200, f"Не удалось удалить курьера {courier_id}"


# Хук для обработки результатов выполнения тестов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield  # Получение результата выполнения теста
    rep = outcome.get_result()  # Получение объекта отчета

    if rep.when == "call" and rep.failed:  # Если тест завершился неудачно
        try:
            # Здесь можно добавить логику для скриншотов
            # если бы у нас был браузер
            pass
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")  # Вывод сообщения об ошибки