import requests

url = "https://restful-booker.herokuapp.com/auth"


class TestAuthAdmin:
    # позитивная проверка:
    def test_positive_auth_admin(self, auth_positive):
        response = requests.post(url, data=auth_positive)
        assert response.status_code == 200, "Status code not equal 200"
        assert "token" in response.text, "Not received token"

    # негативные проверки:
    def test_negative_register_login(self, auth_negative_register_login):
        response = requests.post(url, data=auth_negative_register_login)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with wrong register login"

    def test_negative_register_pass(self, auth_negative_register_pass):
        response = requests.post(url, data=auth_negative_register_pass)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with wrong register pass"

    def test_negative_auth_admin_wrong_pass(self, auth_admin_wrong_pass):
        response = requests.post(url, data=auth_admin_wrong_pass)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with wrong pass"

    def test_negative_auth_admin_wrong_login(self, auth_admin_wrong_login):
        response = requests.post(url, data=auth_admin_wrong_login)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with wrong login"

    def test_negative_auth_admin_wrong_login_pass(self, auth_admin_wrong_login_pass):
        response = requests.post(url, data=auth_admin_wrong_login_pass)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with wrong login and pass"

    def test_negative_auth_admin_empty_login(self, auth_admin_empty_login):
        response = requests.post(url, data=auth_admin_empty_login)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with empty login"

    def test_negative_auth_admin_empty_pass(self, auth_admin_empty_pass):
        response = requests.post(url, data=auth_admin_empty_pass)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with empty pass"

    def test_negative_auth_admin_empty_login_pass(self, auth_admin_empty_login_pass):
        response = requests.post(url, data=auth_admin_empty_login_pass)
        assert response.text == '{"reason":"Bad credentials"}', "Token received  with empty login and pass"
