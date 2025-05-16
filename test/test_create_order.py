import json
import pytest
import requests
import allure
from test_data import Urls, TestData

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

        f = TestData()
        f.test_create_order_dto(colour_list)

        response = requests.post(f"{Urls.base_url}{Urls.api_create_order}", data=json.dumps(f.test_create_order_dto(colour_list)))

        assert response.status_code == 201 and 'track' in response.json()
