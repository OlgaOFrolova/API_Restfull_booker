import requests

url = "https://restful-booker.herokuapp.com/booking/"


class TestDeleteBooking:

    # удаление по существующему ID
    def test_delete_booking_valid_id(self, update_booking_valid_data, update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.delete(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                    json=update_booking_valid_data, headers={'Cookie': update_booking_valid_token})

        expected_status_code = 201
        assert response2.status_code == expected_status_code, \
            f"Unexpected status code! Expected {expected_status_code}. " \
            f"Actual:{response2.status_code}"

    # удаление по несуществующему ID
    def test_delete_booking_invalid_id(self, update_booking_valid_data, id_invalid_data,
                                       update_booking_valid_token):
        response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{id_invalid_data}",
                                   json=update_booking_valid_data, headers={'Cookie': update_booking_valid_token})
        expected_status_code = 405
        assert response.status_code == expected_status_code, f"Unexpected status code! Expected {expected_status_code}. " \
                                                             f"Actual:{response.status_code} Delete invalid ID "

    # удаление по невалидному ID
    def test_delete_booking_nonexistent_id(self, update_booking_valid_data, id_nonexistent_data,
                                           update_booking_valid_token):
        response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{id_nonexistent_data}",
                                   json=update_booking_valid_data, headers={'Cookie': update_booking_valid_token})
        expected_status_code = 405
        assert response.status_code == expected_status_code, f"Unexpected status code! Expected {expected_status_code}. " \
                                                             f"Actual:{response.status_code} Delete nonexistent ID "

    # удаление уже удаленного объекта

    def test_delete_booking_twice(self, update_booking_valid_data, update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.delete(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                    json=update_booking_valid_data, headers={'Cookie': update_booking_valid_token})
        response3 = requests.delete(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                    json=update_booking_valid_data, headers={'Cookie': update_booking_valid_token})
        expected_status_code = 405
        assert response3.status_code == expected_status_code, f"Unexpected status code! Expected {expected_status_code}. " \
                                                              f"Actual:{response3.status_code} Delete deleted ID "
