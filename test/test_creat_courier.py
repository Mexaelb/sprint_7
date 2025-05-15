import pytest
import requests
from test_data import Urls
import allure

class TestCreateCourier:

    @allure.title('Проверка создание курьера')
    def test_create_courier(self,create_courier_dto):

        response = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)
        assert response.json() == {'ok': True}
        assert response.status_code == 201


    @allure.title('Проверка нельзя создать 2х одинаковых курьеров')
    def test_double_create_courier(self,create_courier_dto):

        response1 = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)
        response2 = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)

        assert response1.status_code == 201
        assert response2.status_code == 409


    @pytest.mark.parametrize("missing_field", [
        "login",
        "password",
        "firstName"
    ])
    @allure.title('Проверка создания курьера при передачи всех обязательных полей - {missing_field}')
    def test_all_field_create_courier(self,missing_field,create_courier_dto):

        create_courier_dto.pop(missing_field)

        response = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)

        assert response.status_code == 400


    @allure.title('Проверка создание курьера, запрос возвращает правильный код ответа')
    def test_201_create_courier(self,create_courier_dto):

        response = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)

        assert response.status_code == 201


    @allure.title('Проверка создание курьера, успешный запрос возвращает "ok":true')
    def test_create_courier_ok_response(self,create_courier_dto):

        response = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)
        assert response.json() == {'ok': True}


    @pytest.mark.parametrize("missing_field", [
        "login",
        "password",
        "firstName"
    ])
    @allure.title('Проверка создание курьера, если нет 1 поля, ломается создание')
    def test_create_courier_no_all_fields(self,missing_field,create_courier_dto):

        create_courier_dto.pop(missing_field)

        response = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)

        assert response.status_code == 400


    @allure.title('Проверка создание курьера, если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_courier_double_login(self, create_courier_dto):

        payload2 = {
            "login": create_courier_dto['login'],
            "password": create_courier_dto['password']+'1',
            "firstName": create_courier_dto['firstName']+'1'
        }

        response = requests.post(f"{Urls.base_url}/api/v1/courier", data=create_courier_dto)
        response2 = requests.post(f"{Urls.base_url}/api/v1/courier", data=payload2)

        assert response.status_code == 201
        assert response2.status_code == 409
