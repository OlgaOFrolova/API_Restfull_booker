import requests
url = "https://restful-booker.herokuapp.com/booking/"
class TestUpdateBooking:


    #отправка запроса с валидным токеном
    def test_update_booking_valid_token(self, update_booking_valid_data, update_booking_new_valid_data,
                                        update_booking_valid_token ):
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
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                          json=update_booking_new_valid_data, headers={'Cookie': update_booking_invalid_token})

        assert response2.status_code == 403, f"Wrong response code. Expected 403, actual {response2.status_code} "


    # отправка запроса с  валидным заголовком авторизации
    def test_update_booking_valid_authorization_header(self, update_booking_valid_data, update_booking_new_valid_data,
                                        update_booking_valid_authorization_header ):

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

        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                          json=update_booking_new_valid_data, headers= update_booking_invalid_authorization_header)
        assert response2.status_code == 403, f"Wrong response code. Expected 403, actual {response2.status_code} "


    # отправка запроса с валидным данными

    def test_update_booking_all_valid_data(self, update_booking_valid_data, update_booking_all_valid_data,
                                        update_booking_valid_token ):

        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()

        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                          json=update_booking_all_valid_data, headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_firstname = update_booking_all_valid_data['firstname']
        response_firstname = response_as_dict['firstname']

        expected_lastname = update_booking_all_valid_data['lastname']
        response_lastname = response_as_dict['lastname']

        expected_totalprice = update_booking_all_valid_data['totalprice']
        response_totalprice = response_as_dict['totalprice']

        expected_depositpaid = update_booking_all_valid_data['depositpaid']
        response_depositpaid = response_as_dict['depositpaid']

        expected_checkin = update_booking_all_valid_data['bookingdates']['checkin']
        response_checkin = response_as_dict['bookingdates']['checkin']

        expected_checkout = update_booking_all_valid_data['bookingdates']['checkout']
        response_checkout = response_as_dict['bookingdates']['checkout']

        expected_additionalneeds = update_booking_all_valid_data['additionalneeds']
        response_additionalneeds = response_as_dict['additionalneeds']


        assert response2.status_code == 200, "Wrong response code"

        assert response_firstname == expected_firstname, \
            f"Unexpected firstname! Expected {expected_firstname}. " f"Actual:{response_firstname}"
        assert response_lastname == expected_lastname, \
            f"Unexpected lastname! Expected {expected_lastname}. " f"Actual:{response_lastname}"
        assert response_totalprice == expected_totalprice, \
            f"Unexpected totalprice! Expected {expected_totalprice}. " f"Actual:{response_totalprice}"
        assert response_depositpaid == expected_depositpaid, \
            f"Unexpected depositpaid! Expected {expected_depositpaid}. " f"Actual:{response_depositpaid}"
        assert response_checkin == expected_checkin, \
            f"Unexpected checkin! Expected {expected_checkin}. " f"Actual:{response_checkin}"
        assert response_checkout == expected_checkout, \
            f"Unexpected checkout! Expected {expected_checkout}. " f"Actual:{response_checkout}"
        assert response_additionalneeds == expected_additionalneeds, \
            f"Unexpected additionalneeds! Expected {expected_additionalneeds}. " f"Actual:{response_additionalneeds}"

    # отправка запросов с невалидными данными
    #  невалидное поле firstname
    def test_update_booking_invalid_firstname_data(self,update_booking_valid_data, create_booking_invalid_firstname_data,
                                                   update_booking_valid_token ):

            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                     json=create_booking_invalid_firstname_data,
                                     headers={'Cookie': update_booking_valid_token})

            assert response2.status_code == 400, f"Wrong response code. Expected 403, actual {response2.status_code} "

    #  невалидное поле lastname
    def test_update_booking_invalid_lastname_data(self,update_booking_valid_data, create_booking_invalid_lastname_data,
                                                   update_booking_valid_token ):

            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                     json=create_booking_invalid_lastname_data,
                                     headers={'Cookie': update_booking_valid_token})

            assert response2.status_code == 400, f"Wrong response code. Expected 403, actual {response2.status_code} "

    #  невалидное поле totalprice
    def test_update_booking_invalid_totalprice_data(self, update_booking_valid_data, create_booking_invalid_totalprice_data,
                                                  update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                 json=create_booking_invalid_totalprice_data,
                                 headers={'Cookie': update_booking_valid_token})

        assert response2.status_code == 400, f"Wrong response code. Expected 403, actual {response2.status_code} "

    #  невалидное поле depositpaid
    def test_update_booking_invalid_depositpaid_data(self, update_booking_valid_data,
                                                        create_booking_invalid_depositpaid_data,
                                                        update_booking_valid_token):
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                     json=create_booking_invalid_depositpaid_data,
                                     headers={'Cookie': update_booking_valid_token})

            assert response2.status_code == 400, f"Wrong response code. Expected 403, actual {response2.status_code} "

    #  невалидное поле checkin
    def test_update_booking_invalid_checkin_data(self, update_booking_valid_data,
                                                        create_booking_invalid_checkin_data,
                                                        update_booking_valid_token):
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                     json=create_booking_invalid_checkin_data,
                                     headers={'Cookie': update_booking_valid_token})

            assert response2.status_code == 400, f"Wrong response code. Expected 403, actual {response2.status_code} "

    #  невалидное поле checkout
    def test_update_booking_invalid_checkout_data(self, update_booking_valid_data,
                                                 create_booking_invalid_checkout_data,
                                                 update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.put(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                 json=create_booking_invalid_checkout_data,
                                 headers={'Cookie': update_booking_valid_token})

        assert response2.status_code == 400, f"Wrong response code. Expected 403, actual {response2.status_code} "


    # обновление по невалидному ID
    def test_update_booking_invalid_id(self, update_booking_new_valid_data,id_invalid_data,
                                               update_booking_valid_token):

        response = requests.put(f"https://restful-booker.herokuapp.com/booking/{id_invalid_data}",
                                json=update_booking_new_valid_data, headers={'Cookie': update_booking_valid_token})

        assert response.status_code == 405, "Update by invalid ID "

    # обновление по несуществующему ID
    def test_update_booking_nonexistent_id(self, update_booking_new_valid_data, id_nonexistent_data,
                                        update_booking_valid_token):

        response = requests.put(f"https://restful-booker.herokuapp.com/booking/{id_nonexistent_data}",
                                json=update_booking_new_valid_data, headers={'Cookie': update_booking_valid_token})

        assert response.status_code == 405, "Update by non-existent ID "

