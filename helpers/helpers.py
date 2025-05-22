import allure
from src.courier import CourierClass

@allure.step('удаление курьера')
def delete_courier_by_login(login_password):
    courier = CourierClass()
    response = courier.login_courier(login_password)[1]
    courier_id = response['id']
    courier.delete_courier(courier_id)
