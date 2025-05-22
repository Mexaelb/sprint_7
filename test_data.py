class Urls:
    base_url = "https://qa-scooter.praktikum-services.ru"

    api_create_courier = "/api/v1/courier"
    api_login_courier = "/api/v1/courier/login"
    api_create_order = "/api/v1/orders"
    api_get_order = "/api/v1/orders"
    api_delete_courier = "/api/v1/courier/"
    api_cancel_order = "/api/v1/orders/cancel"


class ResponseData:
    code_409_create = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    code_ok_create = {'ok': True}
    code_400_create = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    code_400_login = {'code': 400, 'message': 'Недостаточно данных для входа'}
    code_404_login = {'code': 404, 'message': 'Учетная запись не найдена'}
