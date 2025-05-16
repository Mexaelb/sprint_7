import requests
from test_data import Urls
import allure
from user_generate import register_new_courier_and_return_login_password

class TestLoginCourier:

    @allure.title('курьер может авторизоваться')
    def test_login_courier(self):

        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)

        assert response.status_code == 200 and 'id' in response.json()


    @allure.title('для авторизации нужно передать все обязательные поля')
    def test_login_courier_all_fields(self):

        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)
        assert response.status_code == 200 and 'id' in response.json()


    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_courier_error_fields(self):

        login_pass = register_new_courier_and_return_login_password()
        login_pass2 = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass2[1],
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
    def test_login_courier_non_user(self,create_courier_dto):

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=create_courier_dto)
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}


    @allure.title('успешный запрос возвращает id')
    def test_login_courier_ok_id(self):

        login_pass = register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
        }

        response = requests.post(f"{Urls.base_url}{Urls.api_login_courier}", data=payload)
        assert response.status_code == 200 and 'id' in response.json()
