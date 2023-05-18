import requests

url = "https://restful-booker.herokuapp.com/booking/"


class TestCreateBooking:

    def test_create_firstname_valid_data(self, create_firstname_valid_data):
        response = requests.post(url, json=create_firstname_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_lastname_valid_data(self, create_lastname_valid_data):
        response = requests.post(url, json=create_lastname_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_totalprice_valid_data(self, create_totalprice_valid_data):
        response = requests.post(url, json=create_totalprice_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_depositpaid_valid_data(self, create_depositpaid_valid_data):
        response = requests.post(url, json=create_depositpaid_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_checkin_valid_data(self, create_checkin_valid_data):
        response = requests.post(url, json=create_checkin_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_checkout_valid_data(self, create_checkout_valid_data):
        response = requests.post(url, json=create_checkout_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_additionalneeds_valid_data(self, create_additionalneeds_valid_data):
        response = requests.post(url, json=create_additionalneeds_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_booking_invalid_firstname_data(self, create_booking_invalid_firstname_data):
        response = requests.post(url, json=create_booking_invalid_firstname_data)
        assert response.status_code == 500, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_booking_invalid_lastname_data(self, create_booking_invalid_lastname_data):
        response = requests.post(url, json=create_booking_invalid_lastname_data)
        assert response.status_code == 500, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_booking_invalid_totalprice_data(self, create_booking_invalid_totalprice_data):
        response = requests.post(url, json=create_booking_invalid_totalprice_data)
        assert response.status_code == 500, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_booking_invalid_depositpaid_data(self, create_booking_invalid_depositpaid_data):
        response = requests.post(url, json=create_booking_invalid_depositpaid_data)
        assert response.status_code == 500, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_booking_invalid_checkin_data(self, create_booking_invalid_checkin_data):
        response = requests.post(url, json=create_booking_invalid_checkin_data)
        assert response.status_code == 500, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_booking_invalid_checkout_data(self, create_booking_invalid_checkout_data):
        response = requests.post(url, json=create_booking_invalid_checkout_data)
        assert response.status_code == 500, f"Wrong response code: expected 200, received {response.status_code}"

# python -m pytest -s tests/test_create_booking.py
