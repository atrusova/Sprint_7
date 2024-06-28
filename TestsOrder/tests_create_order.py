import requests
from data import OrderData
import pytest
import allure


class TestOrder:

    @pytest.mark.parametrize(
        'order_data, result_code, result_text',
        [
            (OrderData.order_data_black_color, OrderData.result_code, OrderData.result_text),
            (OrderData.order_data_gray_color, OrderData.result_code, OrderData.result_text),
            (OrderData.order_data_two_color, OrderData.result_code, OrderData.result_text),
            (OrderData.order_data_without_color, OrderData.result_code, OrderData.result_text)
        ],
        ids=[
            "Order black scooter",
            "Order gray scooter",
            "Order two color scooter",
            "Order scooter without color",
        ]
    )
    @allure.title(f'Проверка успешного создания заказа с указанием одного цвета, нескольких цветов и без указания цвета')
    def test_create_oder_status_201_track_number(self, order_data, result_code, result_text):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=order_data)
        r = response.json()
        assert response.status_code == result_code and r["track"] != result_text

    @allure.title(f'Проверка получения списка заказов')
    def test_get_list_order(self):
        response = requests.get(
            'https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=10&page=0&nearestStation=["110"]')
        r = response.json()
        assert response.status_code == 200 and r["orders"] != ''
