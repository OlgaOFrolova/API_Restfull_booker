import requests

class TestAuthAdmin:

    # позитивная проверка: вход с валидным логином и паролем
    def test_positive_auth_admin(self, auth_pass, auth_log, auth_url):
        data = {"username": auth_log, "password": auth_pass}
        response = requests.post(auth_url, data)
        assert response.status_code == 200, "Status code not equal 200"
        assert "token" in response.text, "Not received token"

    # время ответа

    def test_check_time(self, auth_pass, auth_log, auth_url):
        data = {"username": auth_log, "password": auth_pass}
        response = requests.get(auth_url)
        assert response.elapsed.total_seconds() <= 1, "Response time is more than 1s"


    # вход c пустым полем логина и пароля
    def test_negative_auth_admin_empty_login_pass(self, auth_url,negative_auth_admin_empty_login,
                                                  negative_auth_admin_empty_pass):
        for username in negative_auth_admin_empty_login:
            for password in negative_auth_admin_empty_pass:
                data = {"username": username, "password": password}
                response = requests.post(auth_url, data)
                print(response.text)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with empty login and pass"


    # невалидный логин
    def test_negative_auth_admin_invalid_login(self, negative_auth_admin_invalid_login, auth_pass, auth_url):
        for username in negative_auth_admin_invalid_login:
            data = {"username": username, "password": auth_pass}
            response = requests.post("https://restful-booker.herokuapp.com/auth", data )
            print(response.text)
            assert response.text == '{"reason":"Bad credentials"}', "Token received  with invalid login "

    # невалидный пароль
    def test_negative_auth_admin_invalid_pass(self, negative_auth_admin_invalid_pass, auth_log, auth_url):
        for password in negative_auth_admin_invalid_pass:
            data = {"username":  auth_log, "password": password}
            response = requests.post("https://restful-booker.herokuapp.com/auth", data)
            print(response.text)
            assert response.text == '{"reason":"Bad credentials"}', "Token received  with invalid password "