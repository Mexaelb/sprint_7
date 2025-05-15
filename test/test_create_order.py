import json
import pytest
import requests
from test_data import Urls
import allure

class TestCreateOrder:

    @pytest.mark.parametrize("colour", [
        "BLACK",
        "GREY",
    ])
    @allure.title('можно указать один из цветов — BLACK или GREY')
    def test_create_order_one_color(self,colour):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [colour]
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_create_order}", data=json.dumps(payload))

        assert response.status_code == 201
        assert 'track' in response.json()


    @allure.title('можно указать оба цвета')
    def test_create_order_twice_color(self):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK","GREY"]
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_create_order}", data=json.dumps(payload))

        assert response.status_code == 201
        assert 'track' in response.json()


    @allure.title('можно совсем не указывать цвет')
    def test_create_order_no_color(self):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": []
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_create_order}", data=json.dumps(payload))

        assert response.status_code == 201
        assert 'track' in response.json()
