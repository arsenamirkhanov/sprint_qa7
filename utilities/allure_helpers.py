# Импорт необходимых библиотек
import allure  # Библиотека для создания отчетов Allure
from allure_commons.types import AttachmentType  # Типы вложений для Allure

# Функция для добавления скриншота в отчет Allure
def attach_screenshot(browser, name):
    # Добавление скриншота в отчет
    allure.attach(
        browser.get_screenshot_as_png(),  # Получение скриншота в формате PNG
        name=name,  # Имя вложения
        attachment_type=AttachmentType.PNG  # Тип вложения (PNG)
    )

# Функция для добавления данных ответа в отчет Allure
def attach_response_data(response, name="Response Data"):
    # Проверка наличия текста в ответе
    if response.text:
        # Добавление текста ответа в отчет
        allure.attach(
            response.text,  # Текст ответа
            name=name,  # Имя вложения
            attachment_type=AttachmentType.TEXT  # Тип вложения (текст)
        )

# Функция для добавления данных запроса в отчет Allure
def attach_request_data(request, name="Request Data"):
    # Проверка наличия тела запроса
    if request.body:
        # Добавление тела запроса в отчет
        allure.attach(
            request.body if isinstance(request.body, str) else str(request.body),  # Тело запроса (приводим к строке если нужно)
            name=name,  # Имя вложения
            attachment_type=AttachmentType.TEXT  # Тип вложения (текст)
        )