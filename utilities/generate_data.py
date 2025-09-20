# Импорт необходимых библиотек
import random  # Библиотека для генерации случайных данных
import string  # Библиотека для работы со строками
import requests  # Библиотека для отправки HTTP-запросов
import allure  # Библиотека для создания отчетов Allure


# Функция для генерации случайной строки заданной длины
def generate_random_string(length):
    # Получение всех букв нижнего регистра
    letters = string.ascii_lowercase
    # Генерация случайной строки из букв нижнего регистра
    random_string = ''.join(random.choice(letters) for i in range(length))
    # Возврат сгенерированной строки
    return random_string


# Функция для генерации тестовых данных курьера с добавлением шага в Allure отчет
@allure.step("Генерация тестовых данных курьера")  # Декоратор для добавления шага в отчет
def generate_courier_data():
    # Возврат словаря с тестовыми данными курьера
    return {
        "login": generate_random_string(10),  # Генерация логина длиной 10 символов
        "password": generate_random_string(10),  # Генерация пароля длиной 10 символов
        "firstName": generate_random_string(10)  # Генерация имени длиной 10 символов
    }


# Функция для генерации тестовых данных заказа с добавлением шага в Allure отчет
@allure.step("Генерация тестовых данных заказа")  # Декоратор для добавления шага в отчет
def generate_order_data(color=None):
    # Создание базового набора данных заказа
    base_data = {
        "firstName": generate_random_string(10),  # Генерация имени длиной 10 символов
        "lastName": generate_random_string(10),  # Генерация фамилии длиной 10 символов
        "address": generate_random_string(20),  # Генерация адреса длиной 20 символов
        "metroStation": random.randint(1, 10),  # Генерация случайного номера станции метро
        "phone": "+7999" + ''.join([str(random.randint(0, 9)) for _ in range(7)]),  # Генерация номера телефона
        "rentTime": random.randint(1, 7),  # Генерация времени аренды (1-7 дней)
        "deliveryDate": "2023-12-12",  # Установка даты доставки
        "comment": generate_random_string(30),  # Генерация комментария длиной 30 символов
    }

    # Добавление цвета, если он указан
    if color is not None:
        base_data["color"] = color  # Добавление цвета в данные заказа

    # Возврат данных заказа
    return base_data


# Функция для регистрации нового курьера с добавлением шага в Allure отчет
@allure.step("Регистрация нового курьера")  # Декоратор для добавления шага в отчет
def register_new_courier():
    courier_data = generate_courier_data()
    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier',
        data=courier_data
    )

    if response.status_code == 201:
        return courier_data
    else:
        # Генерируем новые данные при неудаче
        return register_new_courier()

