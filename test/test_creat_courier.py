import requests
import random
import string
from test_data import Urls
import allure
from user_generate import register_new_courier_and_return_login_password


@allure.title('Проверка создание курьера')
def test_create_courier():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)
    assert response.json() == {'ok': True}
    assert response.status_code == 201


@allure.title('Проверка нельзя создать 2х одинаковых курьеров')
def test_double_create_courier():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response1 = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)
    response2 = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)

    assert response1.status_code == 201
    assert response2.status_code == 409

@allure.title('Проверка создания курьера при передачи всех обязательных полей')
def test_all_field_create_courier():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)

    assert response.status_code == 201

@allure.title('Проверка создание курьера, запрос возвращает правильный код ответа')
def test_201_create_courier():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)

    assert response.status_code == 201

@allure.title('Проверка создание курьера, успешный запрос возвращает {"ok":true}')
def test_create_courier_ok_response():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)
    assert response.json() == {'ok': True}

@allure.title('Проверка создание курьера, если нет 1 поля, ломается создание')
def test_create_courier_no_all_fields():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)
    assert response.status_code == 400

@allure.title('Проверка создание курьера, если создать пользователя с логином, который уже есть, возвращается ошибка.')
def test_create_courier_double_login():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    payload2 = {
        "login": login,
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


    response = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload)
    response2 = requests.post(f"{Urls.main_page}/api/v1/courier", data=payload2)

    assert response.status_code == 201
    assert response2.status_code == 409


