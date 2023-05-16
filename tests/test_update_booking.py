import requests

class TestUpdateBooking:

    #отправка запроса с валидным токеном
    def test_update_booking_valid_token(self, update_booking_valid_data, update_booking_new_valid_data,
                                        update_booking_valid_token ):
        url = "https://restful-booker.herokuapp.com/booking/"
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                          json=update_booking_new_valid_data, headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_firstname = update_booking_new_valid_data['firstname']
        response_firstname = response_as_dict['firstname']

        assert response2.status_code == 200, "Wrong response code"
        assert response_firstname == expected_firstname, \
        f"Unexpected firstname! Expected {expected_firstname}. " f"Actual:{response_firstname}"


    # отправка запроса с невалидным токеном
    def test_update_booking_invalid_token(self, update_booking_valid_data, update_booking_new_valid_data,
                                        update_booking_invalid_token ):
        url = "https://restful-booker.herokuapp.com/booking/"
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                          json=update_booking_new_valid_data, headers={'Cookie': update_booking_invalid_token})

        assert response2.status_code == 403, f"Wrong response code. Expected 403, actual {response2.status_code} "


    # отправка запроса с с валидным заголовком авторизации
    def test_update_booking_valid_authorization_header(self, update_booking_valid_data, update_booking_new_valid_data,
                                        update_booking_valid_authorization_header ):

        url = "https://restful-booker.herokuapp.com/booking/"
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                          json=update_booking_new_valid_data, headers= update_booking_valid_authorization_header)

        response_as_dict = response2.json()
        expected_firstname = update_booking_new_valid_data['firstname']
        response_firstname = response_as_dict['firstname']

        assert response2.status_code == 200, "Wrong response code"
        assert response_firstname == expected_firstname, \
        f"Unexpected firstname! Expected {expected_firstname}. " f"Actual:{response_firstname}"

    def test_update_booking_invalid_authorization_header(self, update_booking_valid_data, update_booking_new_valid_data,
                                        update_booking_invalid_authorization_header ):

        url = "https://restful-booker.herokuapp.com/booking/"
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                          json=update_booking_new_valid_data, headers= update_booking_invalid_authorization_header)
        assert response2.status_code == 403, f"Wrong response code. Expected 403, actual {response2.status_code} "


