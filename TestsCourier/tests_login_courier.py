import requests
import allure
from helpers import registration_courier_data_for_login, registration_courier_data_without_login, registration_courier_get_data_without_pass, registration_courier_get_data_incorrect_login, registration_courier_get_data_incorrect_pass


class TestLoginCourier:

    @allure.title(f'Проверка успешного логина курьера')
    def test_login_courier_get_status_200_and_get_id(self):
        registration_data = registration_courier_data_for_login()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=registration_data)
        r = response.json()
        assert response.status_code == 200 and r["id"] != ''

    @allure.title(f'Проверка попытки входа курьера без логина')
    def test_login_courier_without_login_get_status_400_and_text_error(self):
        registration_data = registration_courier_data_without_login()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=registration_data)
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для входа'

    @allure.title(f'Проверка попытки входа курьера без пароля')
    def test_login_courier_without_pass_get_status_400_and_text_error(self):
        registration_data = registration_courier_get_data_without_pass()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=registration_data)
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для входа'

    @allure.title(f'Проверка попытки входа курьера с некорректным логином')
    def test_login_courier_incorrect_login_get_status_400_and_text_error(self):
        registration_data = registration_courier_get_data_incorrect_login()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=registration_data)
        r = response.json()
        assert response.status_code == 404 and r["message"] == 'Учетная запись не найдена'

    @allure.title(f'Проверка попытки входа курьера с некорректным паролем')
    def test_login_courier_incorrect_pass_get_status_400_and_text_error(self):
        registration_data = registration_courier_get_data_incorrect_pass()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=registration_data)
        r = response.json()
        assert response.status_code == 404 and r["message"] == 'Учетная запись не найдена'
