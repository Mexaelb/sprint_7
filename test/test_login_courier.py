import requests
import random
import string
from test_data import Urls
import allure
from user_generate import register_new_courier_and_return_login_password


@allure.title('курьер может авторизоваться')
def test_login_courier():

    login_pass = register_new_courier_and_return_login_password()

    payload = {
        "login": login_pass[0],
        "password": login_pass[1],
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier/login", data=payload)

    assert response.status_code == 200

@allure.title('для авторизации нужно передать все обязательные поля')
def test_login_courier_all_fields():

    login_pass = register_new_courier_and_return_login_password()

    payload = {
        "login": login_pass[0],
        "password": login_pass[1],
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier/login", data=payload)
    assert response.status_code == 200

@allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
def test_login_courier_error_fields():

    login_pass = register_new_courier_and_return_login_password()
    login_pass2 = register_new_courier_and_return_login_password()

    payload = {
        "login": login_pass[0],
        "password": login_pass2[1],
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier/login", data=payload)
    assert response.status_code == 404

@allure.title('если какого-то поля нет, запрос возвращает ошибку')
def test_login_courier_non_login_fields():

    login_pass = register_new_courier_and_return_login_password()

    payload = {
        "password": login_pass[1],
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier/login", data=payload)
    assert response.status_code == 400


@allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;')
def test_login_courier_non_user():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)

    payload = {
        "login": login[0],
        "password": password[1],
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier/login", data=payload)
    assert response.status_code == 404

@allure.title('успешный запрос возвращает id')
def test_login_courier_ok_id():

    login_pass = register_new_courier_and_return_login_password()

    payload = {
        "login": login_pass[0],
        "password": login_pass[1],
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier/login", data=payload)
    assert  'id' in response.json()