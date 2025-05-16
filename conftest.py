import pytest
from src.courier import CourierClass

@pytest.fixture()
def courier_t():

    courier = CourierClass()
    courier.register_new_courier_and_return_login_password()
    yield courier
    courier.delete_courier(id)
