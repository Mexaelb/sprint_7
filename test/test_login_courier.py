import pytest
from helpers.test_data_generation import TestData
from test_data import ResponseData
from src.courier import CourierClass
import allure


class TestLoginCourier:

    @allure.title('курьер может авторизоваться')
    @allure.description('''курьер может авторизоваться,<br>
     для авторизации нужно передать все обязательные поля, <br>
     успешный запрос возвращает id''')
    def test_login_courier(self, login_pass_name):
        courier = CourierClass()

        status_code, response = courier.login_courier(login_pass_name)
        assert status_code == 200 and 'id' in response

    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_courier_error_fields(self, login_pass_name):
        courier = CourierClass()
        payload = {
            "login": login_pass_name['login'],
            "password": login_pass_name['password'] + '1'
        }
        status_code, response = courier.login_courier(payload)

        assert status_code == 404 and response == ResponseData.code_404_login

    @pytest.mark.parametrize("missing_field", [
        "login",
        "password"
    ])
    @allure.title('если какого-то поля нет, запрос возвращает ошибку')
    def test_login_courier_non_login_fields(self, login_pass_name, missing_field):
        courier = CourierClass()
        payload = {
            "login": login_pass_name['login'],
            "password": login_pass_name['password']
        }
        payload.pop(missing_field)
        status_code, response = courier.login_courier(payload)
        assert status_code == 400 and response == ResponseData.code_400_login

    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;')
    def test_login_courier_non_user(self):
        dto_payload = TestData()
        login_pass = dto_payload.login_pass_name_courier_dto()
        courier = CourierClass()
        status_code, response = courier.login_courier(login_pass)
        assert status_code == 404 and response == ResponseData.code_404_login
