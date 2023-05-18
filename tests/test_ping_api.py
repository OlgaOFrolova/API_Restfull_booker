import requests

url = "https://restful-booker.herokuapp.com/ping"


class TestPing:
    def test_ping(self):
        response = requests.get(url)
        expected_status_code = 201
        assert response.status_code == expected_status_code, f"Unexpected status code! Expected {expected_status_code}. " \
                                                             f"Actual:{response.status_code} API is`not up and running "
