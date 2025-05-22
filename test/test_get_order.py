import allure
from src.order import OrderClass


class TestGetOrder:

    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    def test_get_order(self):
        get_order = OrderClass()
        status_code, response = get_order.get_order()
        assert status_code == 200 and 'orders' in response
