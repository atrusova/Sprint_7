import requests
import random
import string
import allure


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.title(f'Данные для регистрации, все данные')
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

@allure.title(f'Данные для регистрации курьера без логина')
def registration_courier_data_without_login():
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "password": password,
        "firstName": first_name
    }
    return payload

@allure.title(f'Данные для регистрации курьера без пароля')
def registration_courier_data_without_pass():
    login = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "firstName": first_name
    }
    return payload

@allure.title(f'Регистрируем курьера, возвращаем данные для регистрации курьера без логина')
def registration_courier_data_for_login():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    login_pass = {}

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass["login"] = login
        login_pass["password"] = password

    # возвращаем список
    return login_pass

@allure.title(f'Регистрируем курьера, возвращаем данные для регистрации курьера без пароля')
def registration_courier_get_data_without_pass():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса для регистрации
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    data_without_pass = {}

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        data_without_pass["login"] = login
        data_without_pass["password"] = ''
        data_without_pass["first_name"] = first_name

    # возвращаем список
    return data_without_pass

@allure.title(f'Регистрируем курьера, возвращаем данные для регистрации курьера с некорректным логином')
def registration_courier_get_data_incorrect_login():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса для регистрации
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    data_incorrect_login = {}
    incorrect_login = f'{login + login}'

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        data_incorrect_login["login"] = incorrect_login
        data_incorrect_login["password"] = password
        data_incorrect_login["first_name"] = first_name

    # возвращаем список
    return data_incorrect_login

@allure.title(f'Регистрируем курьера, возвращаем данные для регистрации курьера с некорректным паролем')
def registration_courier_get_data_incorrect_pass():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса для регистрации
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    data_incorrect_pass = {}
    incorrect_pass = f'{password + password}'

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        data_incorrect_pass["login"] = login
        data_incorrect_pass["password"] = incorrect_pass
        data_incorrect_pass["first_name"] = first_name

    # возвращаем список
    return data_incorrect_pass

