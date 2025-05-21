import pytest
from src.courier import CourierClass
from helpers.helpers import delete_courier_by_login


@pytest.fixture()
def login_pass_name():

    courier = CourierClass()
    login_pass_name = courier.register_new_courier_and_return_login_password()
    yield login_pass_name
    delete_courier_by_login(login_pass_name)
