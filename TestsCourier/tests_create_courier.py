import requests
import allure
from helpers import registration_courier_full_data, registration_courier_data_without_login, registration_courier_data_without_pass


class TestCreateCourier:

    @allure.title(f'Проверка успешного создания курьера')
    def test_register_new_courier_full_data_return_200_and_text_true(self):
        registration_data = registration_courier_full_data()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=registration_data)
        r = response.json()
        assert response.status_code == 201 and r["ok"] == True

    @allure.title(f'Проверка получения ошибки при попытке создания двух одинаковых курьеров')
    def test_register_two_same_login_return_error(self):
        registration_data = registration_courier_full_data()
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=registration_data)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=registration_data)
        assert response.status_code == 409

    @allure.title(f'Проверка получения ошибки при попытке создания курьера без логина')
    def test_register_new_courier_without_login_return_error_text(self):
        registration_data = registration_courier_data_without_login()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=registration_data)
        r = response.json()
        assert r["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title(f'Проверка получения ошибки при попытке создания курьера без пароля')
    def test_register_new_courier_without_pass_return_error_text(self):
        registration_data = registration_courier_data_without_pass()
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=registration_data)
        r = response.json()
        assert r["message"] == "Недостаточно данных для создания учетной записи"
