import requests
import allure
import json
from data import Url, TextsError
from helpers import registration_courier_get_data_for_login


class TestLoginCourier:

    @allure.title(f'Проверка успешного логина курьера')
    def test_login_courier_get_status_200_and_get_id(self):
        registration_data = registration_courier_get_data_for_login()
        response = requests.post(Url.url_login_courier, data=registration_data)
        r = response.json()
        assert response.status_code == 200 and r["id"] != ''

    @allure.title(f'Проверка попытки входа курьера без логина')
    def test_login_courier_without_login_get_status_400_and_text_error(self):
        registration_data = registration_courier_get_data_for_login()
        registration_data["login"] = ''
        response = requests.post(Url.url_login_courier, data=registration_data)
        r = response.json()
        assert response.status_code == 400 and r["message"] == TextsError.not_full_data_for_login

    @allure.title(f'Проверка попытки входа курьера без пароля')
    def test_login_courier_without_pass_get_status_400_and_text_error(self):
        registration_data = registration_courier_get_data_for_login()
        registration_data["password"] = ''
        response = requests.post(Url.url_login_courier, data=registration_data)
        r = response.json()
        assert response.status_code == 400 and r["message"] == TextsError.not_full_data_for_login

    @allure.title(f'Проверка попытки входа курьера с некорректным логином')
    def test_login_courier_incorrect_login_get_status_400_and_text_error(self):
        registration_data = registration_courier_get_data_for_login()
        registration_data["login"] = 'qwerty'
        response = requests.post(Url.url_login_courier, data=registration_data)
        r = response.json()
        assert response.status_code == 404 and r["message"] == TextsError.account_not_found

    @allure.title(f'Проверка попытки входа курьера с некорректным паролем')
    def test_login_courier_incorrect_pass_get_status_400_and_text_error(self):
        registration_data = registration_courier_get_data_for_login()
        registration_data["password"] = 'qwerty'
        response = requests.post(Url.url_login_courier, data=registration_data)
        r = response.json()
        assert response.status_code == 404 and r["message"] == TextsError.account_not_found
