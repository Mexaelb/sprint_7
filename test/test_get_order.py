import requests
from test_data import Urls
import allure

class TestGetOrder:

    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    def test_get_order(self):

            response = requests.get(f"{Urls.base_url}{Urls.api_get_order}")

            assert response.status_code == 200 and 'orders' in response.json()
