class Urls:

    base_url = "https://qa-scooter.praktikum-services.ru"

    api_create_courier = "/api/v1/courier"
    api_login_courier = "/api/v1/courier/login"
    api_create_order = "/api/v1/orders"
    api_get_order = "/api/v1/orders"

class TestData:

    def test_create_order_dto(self, colour_list):

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