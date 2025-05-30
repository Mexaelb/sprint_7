import string
import random
import allure


class TestData:

    @staticmethod
    @allure.step('получение тестовых данных заказа')
    def create_order_dto(colour_list):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour_list
        }

        return payload

    @staticmethod
    @allure.step('создание логин/пароль/имя курьера')
    def login_pass_name_courier_dto():
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

        return payload
