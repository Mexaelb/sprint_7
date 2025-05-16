import requests
from test_data import Urls, TestData
from src.courier import CourierClass
import allure
from user_generate import register_new_courier_and_return_login_password

class TestLoginCourier:

    @allure.title('курьер может авторизоваться')
    def test_login_courier(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier()
        assert status_code == 200 and 'id' in response

        courier_id = response['id']
        login_pass.delete_courier(courier_id)


    @allure.title('для авторизации нужно передать все обязательные поля')
    def test_login_courier_all_fields(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier()
        assert status_code == 200 and 'id' in response

        courier_id = response['id']
        login_pass.delete_courier(courier_id)


    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_courier_error_fields(self):

        login_pass = CourierClass()
        u = login_pass.register_new_courier_and_return_login_password()
        u2 = login_pass.register_new_courier_and_return_login_password()

        payload = {
            "login": u['login'],
            "password": u2['password'],
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)

        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}


    @allure.title('если какого-то поля нет, запрос возвращает ошибку')
    def test_login_courier_non_login_fields(self):

        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "password": login_pass[1],
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)

        assert response.status_code == 400


    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;')
    def test_login_courier_non_user(self):

        ff = TestData()
        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=ff.login_pass_name_courier_dto())

        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}


    @allure.title('успешный запрос возвращает id')
    def test_login_courier_ok_id(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier()
        assert status_code == 200 and 'id' in response

        courier_id = response['id']
        login_pass.delete_courier(courier_id)
