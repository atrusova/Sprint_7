import requests
import allure
import json
from data import Url, TextsError
from helpers import registration_courier_full_data


class TestCreateCourier:

    @allure.title(f'Проверка успешного создания курьера')
    def test_register_new_courier_full_data_return_200_and_text_true(self):
        registration_data = registration_courier_full_data()
        response = requests.post(Url.url_create_courier, data=registration_data)
        r = response.json()
        assert response.status_code == 201 and r["ok"] == True

    @allure.title(f'Проверка получения ошибки при попытке создания двух одинаковых курьеров')
    def test_register_two_same_login_return_error(self):
        registration_data = registration_courier_full_data()
        requests.post(Url.url_create_courier, data=registration_data)
        response = requests.post(Url.url_create_courier, data=registration_data)
        r = response.json()
        assert response.status_code == 409 and r['message'] == TextsError.login_already_used

    @allure.title(f'Проверка получения ошибки при попытке создания курьера без логина')
    def test_register_new_courier_without_login_return_error_text(self):
        registration_data = registration_courier_full_data()
        del registration_data['login']
        registration_data_json = json.dumps(registration_data)
        response = requests.post(Url.url_create_courier, data=registration_data_json)
        r = response.json()
        assert response.status_code == 400 and r["message"] == TextsError.not_full_data_for_registration

    @allure.title(f'Проверка получения ошибки при попытке создания курьера без пароля')
    def test_register_new_courier_without_pass_return_error_text(self):
        registration_data = registration_courier_full_data()
        del registration_data['password']
        registration_data_json = json.dumps(registration_data)
        response = requests.post(Url.url_create_courier, data=registration_data_json)
        r = response.json()
        assert response.status_code == 400 and r["message"] == TextsError.not_full_data_for_registration
