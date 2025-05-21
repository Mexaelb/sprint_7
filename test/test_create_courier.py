import pytest
import requests
import allure
from test_data import Urls, ResponseData
from helpers.test_data_generation import TestData
from helpers.helpers import delete_courier_by_login
from src.courier import CourierClass


class TestCreateCourier:

    @allure.title('Проверка создание курьера')
    @allure.description('1. запрос возвращает правильный код ответа 2. успешный запрос возвращает "ok":true')
    def test_create_courier(self):
        courier = CourierClass()
        status_code, response, login_pass = courier.register_new_courier_and_return_lp()
        assert status_code == 201 and response == ResponseData.code_ok_create
        delete_courier_by_login(login_pass)

    @allure.title('Проверка нельзя создать 2х одинаковых курьеров')
    def test_double_create_courier(self, login_pass_name):
        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass_name)

        assert response.status_code == 409 and response.json() == ResponseData.code_409_create

    @pytest.mark.parametrize("missing_field", [
        "login",
        "password",
        "firstName"
    ])
    @allure.title('Проверка создания курьера при передачи всех обязательных полей - {missing_field}')
    def test_all_field_create_courier(self, missing_field):
        ff = TestData()
        login_pass = ff.login_pass_name_courier_dto()
        login_pass.pop(missing_field)
        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass)
        assert response.status_code == 400 and response.json() == ResponseData.code_400_create

    @pytest.mark.parametrize("missing_field", [
        "login",
        "password",
        "firstName"
    ])
    @allure.title('Проверка создание курьера, если нет 1 поля, ломается создание')
    def test_create_courier_no_all_fields(self, missing_field):
        ff = TestData()
        login_pass = ff.login_pass_name_courier_dto()
        login_pass.pop(missing_field)
        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass)
        assert response.status_code == 400 and response.json() == ResponseData.code_400_create

    @allure.title('Проверка создание курьера, если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_courier_double_login(self, login_pass_name):
        payload2 = {
            "login": login_pass_name['login'],
            "password": login_pass_name['password'] + '1',
            "firstName": login_pass_name['firstName'] + '1'
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=payload2)
        assert response.status_code == 409 and response.json() == ResponseData.code_409_create
