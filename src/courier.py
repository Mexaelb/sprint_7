import json

import requests
import allure
from requests import ReadTimeout

from test_data import Urls
from helpers.test_data_generation import TestData


class CourierClass:

    @allure.step('регистрация нового курьера')
    def register_new_courier_and_return_login_password(self):
        dto_payload = TestData()
        login_pass_name = dto_payload.login_pass_name_courier_dto()
        response = requests.post(f'{Urls.base_url}{Urls.api_create_courier}', data=login_pass_name)
        assert response.status_code == 201 and response.json() == {'ok': True}
        return login_pass_name

    @allure.step('удаление курьера')
    def delete_courier(self, courier_id):
        requests.delete(f'{Urls.base_url}{Urls.api_delete_courier}{courier_id}')

    @allure.step('авторизация курьера')
    def login_courier(self, login_pass_name: dict):
        timeout = 10
        response = None
        payload = {
            "login": login_pass_name.get('login', None),
            "password": login_pass_name.get('password', None)
        }
        try:
            response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload, timeout=timeout)
            return response.status_code, response.json()
        except json.decoder.JSONDecodeError:
            raise AssertionError(f'невозможно получить тело ответа - status code: {response.status_code}')
        except ReadTimeout:
            raise AssertionError(f'запрос выполнялся дольше: {timeout} сек.')

    @allure.step('авторизоваться под несуществующим пользователем')
    def login_courier_non_user(self):
        dto_payload = TestData()
        login_pass_name = dto_payload.login_pass_name_courier_dto()

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=login_pass_name)
        return response.status_code, response.json()

    @allure.step('регистрация нового курьера')
    def register_new_courier_and_return_lp(self):
        dto_payload = TestData()
        login_pass_name = dto_payload.login_pass_name_courier_dto()
        response = requests.post(f'{Urls.base_url}{Urls.api_create_courier}', data=login_pass_name)

        return response.status_code, response.json(), login_pass_name
