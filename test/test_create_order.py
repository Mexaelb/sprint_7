import pytest
import allure
from src.order import OrderClass


class TestCreateOrder:

    @pytest.mark.parametrize("colour_list", [
        ["BLACK"],
        ["GREY"],
        ["BLACK",
         "GREY", ],
        []
    ])
    @allure.title('можно создать заказ с такими цветами — {colour_list}')
    def test_create_order_color(self, colour_list):
        create_order = OrderClass()
        status_code, response = create_order.create_order(colour_list)

        assert status_code == 201 and 'track' in response
