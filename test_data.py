import string
import random

class Urls:

    base_url = "https://qa-scooter.praktikum-services.ru"

    api_create_courier = "/api/v1/courier"
    api_login_courier = "/api/v1/courier/login"
    api_create_order = "/api/v1/orders"
    api_get_order = "/api/v1/orders"

class TestData:

    @staticmethod
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