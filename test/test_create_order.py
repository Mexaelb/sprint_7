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
    def test_create_order_color(self,colour_list,test_create_order_dto):

        response = requests.post(f"{Urls.base_url}{Urls.api_create_order}", data=json.dumps(test_create_order_dto))

        assert response.status_code == 201 and 'track' in response.json()
