import pytest
import requests
from test_data import Urls, TestData
import allure

class TestCreateCourier:

    @allure.title('Проверка создание курьера')
    def test_create_courier(self):

        ff = TestData()

        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=ff.login_pass_name_courier_dto())
        assert response.json() == {'ok': True} and response.status_code == 201


    @allure.title('Проверка нельзя создать 2х одинаковых курьеров')
    def test_double_create_courier(self):

        ff = TestData()
        login_pass = ff.login_pass_name_courier_dto()

        response1 = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass)
        response2 = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass)

        assert response1.status_code == 201 and response1.json() == {'ok': True}
        assert response2.status_code == 409 and response2.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}


    @pytest.mark.parametrize("missing_field", [
        "login",
        "password",
        "firstName"
    ])
    @allure.title('Проверка создания курьера при передачи всех обязательных полей - {missing_field}')
    def test_all_field_create_courier(self,missing_field):

        ff = TestData()
        login_pass = ff.login_pass_name_courier_dto().pop(missing_field)

        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass)

        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}



    @allure.title('Проверка создание курьера, запрос возвращает правильный код ответа')
    def test_201_create_courier(self):

        ff = TestData()

        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=ff.login_pass_name_courier_dto())

        assert response.status_code == 201 and response.json() == {'ok': True}


    @allure.title('Проверка создание курьера, успешный запрос возвращает "ok":true')
    def test_create_courier_ok_response(self):

        ff = TestData()

        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=ff.login_pass_name_courier_dto())
        assert response.status_code == 201 and response.json() == {'ok': True}


    @pytest.mark.parametrize("missing_field", [
        "login",
        "password",
        "firstName"
    ])
    @allure.title('Проверка создание курьера, если нет 1 поля, ломается создание')
    def test_create_courier_no_all_fields(self,missing_field):

        ff = TestData()
        login_pass = ff.login_pass_name_courier_dto().pop(missing_field)

        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass)

        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}


    @allure.title('Проверка создание курьера, если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_courier_double_login(self):

        ff = TestData()
        login_pass = ff.login_pass_name_courier_dto()

        payload2 = {
            "login": login_pass['login'],
            "password": login_pass['password']+'1',
            "firstName": login_pass['firstName']+'1'
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=login_pass)
        response2 = requests.post(f"{Urls.base_url}{Urls.api_create_courier}", data=payload2)

        assert response.status_code == 201 and response.json() == {'ok': True}
        assert response2.status_code == 409 and response2.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
