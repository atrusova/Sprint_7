import requests
import random
import string
import allure
from data import Url


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step(f'Генерируем данные для регистрации')
def registration_courier_full_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

@allure.step(f'Регистрируем курьера, возвращаем данные для регистрации курьера')
def registration_courier_get_data_for_login():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(Url.url_create_courier, data=payload)

    login_pass = {}

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass["login"] = login
        login_pass["password"] = password
        login_pass["first_name"] = first_name

    # возвращаем список
    return login_pass


