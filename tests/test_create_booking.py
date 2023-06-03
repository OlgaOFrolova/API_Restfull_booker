import requests

class TestCreateBooking:

    def test_create_firstname_valid_data(self, booking_url, create_firstname_valid_data):
        for firstname in create_firstname_valid_data:

            data = {"firstname": firstname,
                    "lastname": "Smith",
                    "totalprice": 1000,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-10", "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_firstname_invalid_data(self, booking_url, create_firstname_invalid_data):
        for firstname in create_firstname_invalid_data:
            data = {"firstname": firstname,
                    "lastname": "Smith",
                    "totalprice": 1000,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-10", "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 500, f"Wrong response code: expected 500, received {response.status_code}"

    def test_create_lastname_valid_data(self, booking_url, create_lastname_valid_data):
        for lastname in create_lastname_valid_data:

            data = {"firstname": "John",
                    "lastname": lastname,
                    "totalprice": 1000,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-10", "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"
    def test_create_lastname_invalid_data(self, booking_url, create_lastname_invalid_data):
        for lastname in create_lastname_invalid_data:
            data = {"firstname": "John",
                    "lastname": lastname,
                    "totalprice": 1000,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-10", "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 500, f"Wrong response code: expected 500, received {response.status_code}"

    def test_create_totalprice_valid_data(self, booking_url, create_totalprice_valid_data):
        for totalprice in create_totalprice_valid_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": totalprice,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-10", "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_totalprice_invalid_data(self, booking_url, create_totalprice_invalid_data):
        response = requests.post(booking_url, json=create_totalprice_invalid_data)
        assert response.status_code == 500, f"Wrong response code: expected 500, received {response.status_code}"

    def test_create_depositpaid_valid_data(self,booking_url, create_depositpaid_valid_data):
        response = requests.post(booking_url, json=create_depositpaid_valid_data)
        assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_depositpaid_invalid_data(self,booking_url, create_depositpaid_invalid_data):
        response = requests.post(booking_url, json=create_depositpaid_invalid_data)
        assert response.status_code == 500, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_checkin_valid_data(self, booking_url, create_checkin_valid_data):
        for checkin in create_checkin_valid_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates": {"checkin": checkin, "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_checkin_invalid_data(self, booking_url, create_checkin_invalid_data):
        for checkin in create_checkin_invalid_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates": {"checkin": checkin, "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert "0NaN-aN-aN" in response.text, "Wrong checkin data "
    def test_create_checkin_none_data(self, booking_url, create_checkin_none_data):
        for checkin in create_checkin_none_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates": {"checkin": checkin, "checkout": "2023-03-20"},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 500, f"Wrong response code: expected 400, received {response.status_code}"

    def test_create_checkout_valid_data(self, booking_url, create_checkout_valid_data):
        for checkout in create_checkout_valid_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-20", "checkout": checkout},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"

    def test_create_checkout_invalid_data(self, booking_url, create_checkout_invalid_data):
        for checkout in create_checkout_invalid_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-20", "checkout": checkout},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert "0NaN-aN-aN" in response.text, "Wrong checkout data "

    def test_create_checkout_none_data(self, booking_url, create_checkout_none_data):
        for checkout in create_checkout_none_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-20", "checkout":checkout},
                    "additionalneeds": "Breakfast"}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 500, f"Wrong response code: expected 400, received {response.status_code}"

    def test_create_additionalneeds_valid_data(self, booking_url, create_additionalneeds_valid_data):
        for additionalneeds in create_additionalneeds_valid_data:
            data = {"firstname": "John",
                    "lastname": "Smith",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates": {"checkin": "2023-03-15", "checkout": "2023-03-20"},
                    "additionalneeds": additionalneeds}

            response = requests.post(booking_url, json=data)
            assert response.status_code == 200, f"Wrong response code: expected 200, received {response.status_code}"