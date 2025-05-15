import json
import pytest
import requests
from test_data import Urls
import allure

class TestCreateOrder:

    @pytest.mark.parametrize("colour_list", [
        ["BLACK"],
        ["GREY"],
        ["BLACK",
        "GREY",],
        []

    ])
    @allure.title('можно создать заказ с такими цветами — {colour_list}')
    def test_create_order_color(self,colour_list):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour_list
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_create_order}", data=json.dumps(payload))

        assert response.status_code == 201
        assert 'track' in response.json()
