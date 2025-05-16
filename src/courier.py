import requests
import allure
from test_data import Urls, TestData

class CourierClass:

    @allure.step('регистрация нового курьера')
    def register_new_courier_and_return_login_password(self):
        dto_payload = TestData()
        login_pass_name = dto_payload.login_pass_name_courier_dto()
        requests.post(f'{Urls.base_url}{Urls.api_create_courier}', data=login_pass_name)

        return login_pass_name

    @allure.step('удаление курьера')
    def delete_courier(self, courier_id):
        requests.delete(f'{Urls.base_url}{Urls.api_delete_courier}{courier_id}')

    @allure.step('авторизация курьера')
    def login_courier(self):

        login_pass = CourierClass()
        f = login_pass.register_new_courier_and_return_login_password()

        payload = {
            "login": f['login'],
            "password": f['password'],
        }
        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)
        return response.status_code, response.json()