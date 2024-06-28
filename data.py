class Url:
    url_create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    url_login_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    url_create_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    url_get_order_list = 'https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=10&page=0&nearestStation=["110"]'

class TextsError:
    login_already_used = "Этот логин уже используется. Попробуйте другой."
    not_full_data_for_registration = "Недостаточно данных для создания учетной записи"
    not_full_data_for_login = 'Недостаточно данных для входа'
    account_not_found = 'Учетная запись не найдена'


class OrderData:
    order_data_black_color = {
        "firstName": "Anastasiia",
        "lastName": "Ivanova",
        "address": "Gorkogo 4",
        "metroStation": 4,
        "phone": "+7 8097875577",
        "rentTime": 10,
        "deliveryDate": "2024-09-01",
        "comment": "Call before delivery",
        "color": ["BLACK"]
    }

    order_data_gray_color = {
        "firstName": "Anastasiia",
        "lastName": "Ivanova",
        "address": "Gorkogo 4",
        "metroStation": 4,
        "phone": "+7 8097875577",
        "rentTime": 10,
        "deliveryDate": "2024-09-01",
        "comment": "Call before delivery",
        "color": ["GREY"]
    }

    order_data_two_color = {
        "firstName": "Anastasiia",
        "lastName": "Ivanova",
        "address": "Gorkogo 4",
        "metroStation": 4,
        "phone": "+7 8097875577",
        "rentTime": 10,
        "deliveryDate": "2024-09-01",
        "comment": "Call before delivery",
        "color": ["BLACK", "GREY"]
    }

    order_data_without_color = {
        "firstName": "Anastasiia",
        "lastName": "Ivanova",
        "address": "Gorkogo 4",
        "metroStation": 4,
        "phone": "+7 8097875577",
        "rentTime": 10,
        "deliveryDate": "2024-09-01",
        "comment": "Call before delivery",
        "color": []
    }

    result_code = 201
    result_text = ''
