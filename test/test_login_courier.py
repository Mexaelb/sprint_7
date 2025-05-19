from src.courier import CourierClass
import allure

class TestLoginCourier:

    @allure.title('курьер может авторизоваться')
    @allure.description('''курьер может авторизоваться,
     для авторизации нужно передать все обязательные поля, 
     успешный запрос возвращает id''')
    def test_login_courier(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier()
        assert status_code == 200 and 'id' in response

        courier_id = response['id']
        login_pass.delete_courier(courier_id)


    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_courier_error_fields(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_error_fields()

        assert status_code == 404 and  response == {'code': 404, 'message': 'Учетная запись не найдена'}


    @allure.title('если какого-то поля нет, запрос возвращает ошибку')
    def test_login_courier_non_login_fields(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_non_login_fields()
        assert status_code == 400


    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;')
    def test_login_courier_non_user(self):

        login_pass = CourierClass()
        status_code, response = login_pass.login_courier_non_user()

        assert status_code == 404 and response == {'code': 404, 'message': 'Учетная запись не найдена'}
