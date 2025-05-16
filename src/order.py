import requests
import json
import allure
from test_data import Urls, TestData


class OrderClass:

    @allure.step('создание нового заказа')
    def create_order(self, colour_list):

        f = TestData()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_order}", data=json.dumps(f.create_order_dto(colour_list)))
        return response.status_code, response.json()

    @allure.step('отмена заказа')
    def cancel_order(self,track_id):

        payload ={
            "track": track_id
        }

        requests.delete(f'{Urls.base_url}{Urls.api_cancel_order}', data=payload)

    @allure.step('получение списка заказов')
    def get_order(self):

        response = requests.get(f"{Urls.base_url}{Urls.api_get_order}")
        return response.status_code, response.json()
