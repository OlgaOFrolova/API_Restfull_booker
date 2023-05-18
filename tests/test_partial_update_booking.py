import requests

url = "https://restful-booker.herokuapp.com/booking/"


class TestPartialUpdateBooking:

    # проверка по полю  firstname
    def test_update_booking_Partial_valid_firstname(self, update_booking_valid_data,
                                                    partial_update_booking_valid_firstname,
                                                    update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                   json=partial_update_booking_valid_firstname,
                                   headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_firstname = partial_update_booking_valid_firstname['firstname']
        response_firstname = response_as_dict['firstname']
        assert response2.status_code == 200, "Wrong response code"
        assert response_firstname == expected_firstname, \
            f"Unexpected firstname! Expected {expected_firstname}. " f"Actual:{response_firstname}"

    # проверка по полю  laststname
    def test_update_booking_Partial_valid_lastname(self, update_booking_valid_data,
                                                   partial_update_booking_valid_lastname,
                                                   update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                   json=partial_update_booking_valid_lastname,
                                   headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_lastname = partial_update_booking_valid_lastname['lastname']
        response_lastname = response_as_dict['lastname']
        assert response2.status_code == 200, "Wrong response code"
        assert response_lastname == expected_lastname, \
            f"Unexpected lastname! Expected {expected_lastname}. " f"Actual:{response_lastname}"

    # проверка по полю  totalprice
    def test_update_booking_Partial_valid_lastname(self, update_booking_valid_data,
                                                   partial_update_booking_valid_totalprice,
                                                   update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                   json=partial_update_booking_valid_totalprice,
                                   headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_totalprice = partial_update_booking_valid_totalprice['totalprice']
        response_totalprice = response_as_dict['totalprice']
        assert response2.status_code == 200, "Wrong response code"
        assert response_totalprice == expected_totalprice, \
            f"Unexpected totalprice! Expected {expected_totalprice}. " f"Actual:{response_totalprice}"

    # проверка по полю  depositpaid
    def test_update_booking_Partial_valid_depositpaid(self, update_booking_valid_data,
                                                      partial_update_booking_valid_depositpaid,
                                                      update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                   json=partial_update_booking_valid_depositpaid,
                                   headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_depositpaid = partial_update_booking_valid_depositpaid['depositpaid']
        response_depositpaid = response_as_dict['depositpaid']
        assert response2.status_code == 200, "Wrong response code"
        assert response_depositpaid == expected_depositpaid, \
            f"Unexpected depositpaid! Expected {expected_depositpaid}. " f"Actual:{response_depositpaid}"

    # проверка по полю checkin
    def test_update_booking_Partial_valid_checkin(self, update_booking_valid_data,
                                                  partial_update_booking_valid_checkin,
                                                  update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                   json=partial_update_booking_valid_checkin,
                                   headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_checkin = partial_update_booking_valid_checkin['bookingdates']['checkin']
        response_checkin = response_as_dict['bookingdates']['checkin']
        assert response2.status_code == 200, "Wrong response code"
        assert response_checkin == expected_checkin, \
            f"Unexpected checkin! Expected {expected_checkin}. " f"Actual:{response_checkin}"

    # проверка по полю checkout
    def test_update_booking_Partial_valid_checkout(self, update_booking_valid_data,
                                                   partial_update_booking_valid_checkout,
                                                   update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                   json=partial_update_booking_valid_checkout,
                                   headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_checkout = partial_update_booking_valid_checkout['bookingdates']['checkout']
        response_checkout = response_as_dict['bookingdates']['checkout']
        assert response2.status_code == 200, "Wrong response code"
        assert response_checkout == expected_checkout, \
            f"Unexpected checkin! Expected {expected_checkout}. " f"Actual:{response_checkout}"

    # проверка по полю  additionalneeds
    def test_update_booking_Partial_valid_additionalneeds(self, update_booking_valid_data,
                                                          partial_update_booking_valid_additionalneeds,
                                                          update_booking_valid_token):
        response1 = requests.post(url, json=update_booking_valid_data)
        response_as_dict = response1.json()
        response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                   json=partial_update_booking_valid_additionalneeds,
                                   headers={'Cookie': update_booking_valid_token})

        response_as_dict = response2.json()
        expected_additionalneeds = partial_update_booking_valid_additionalneeds['additionalneeds']
        response_additionalneeds = response_as_dict['additionalneeds']
        assert response2.status_code == 200, "Wrong response code"
        assert response_additionalneeds == expected_additionalneeds, \
            f"Unexpected depositpaid! Expected {expected_additionalneeds}, actual:{response_additionalneeds}"

  # отправка запросов с невалидными данными
    #  невалидное поле firstname
    def test_partial_update_booking_invalid_firstname(self, update_booking_valid_data,
                                                      partial_update_booking_invalid_firstname,
                                                      update_booking_valid_token):
        for response2 in partial_update_booking_invalid_firstname:
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                       json=partial_update_booking_invalid_firstname,
                                       headers={'Cookie': update_booking_valid_token})

            assert response2.status_code != 200, f"Wrong response code. Expected not 200, actual {response2.status_code} "

    '''↑🐞 Bag: при вводе невалидных значений перезаписывает поле "firstname" как 5, 5.5, {"name1":"name2"},  ['name1', 'name2'], true;
       при вводе невалидного значения None - записывает в поле как null '''


    # невалидное поле lastname
    def test_partial_update_booking_invalid_lastname(self, update_booking_valid_data,
                                                     partial_update_booking_invalid_lastname,
                                                     update_booking_valid_token):
        for response2 in partial_update_booking_invalid_lastname:
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                       json=partial_update_booking_invalid_lastname,
                                       headers={'Cookie': update_booking_valid_token})
            assert response2.status_code != 200, f"Wrong response code. Expected not 200, actual {response2.status_code} "

    '''↑🐞 Bag '''


    # #  невалидное поле totalprice
    def test_partial_update_booking_invalid_totalprice(self, update_booking_valid_data,
                                                       partial_update_booking_invalid_totalprice,
                                                       update_booking_valid_token):
        for response2 in partial_update_booking_invalid_totalprice:
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                       json=partial_update_booking_invalid_totalprice,
                                       headers={'Cookie': update_booking_valid_token})
            assert response2.status_code != 200, f"Wrong response code. Expected not 200, actual {response2.status_code} "

    '''↑🐞 Bag '''


    #  невалидное поле depositpaid
    def test_partial_update_booking_invalid_depositpaid(self, update_booking_valid_data,
                                                        partial_update_booking_invalid_depositpaid,
                                                        update_booking_valid_token):
        for response2 in partial_update_booking_invalid_depositpaid:
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.patch(
                f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                json=partial_update_booking_invalid_depositpaid,
                headers={'Cookie': update_booking_valid_token})
            assert response2.status_code != 200, f"Wrong response code. Expected not 200, actual {response2.status_code}"

    '''↑🐞 Bag '''


    # невалидное поле checkin
    def test_partial_update_booking_invalid_checkin(self, update_booking_valid_data,
                                                    partial_update_booking_invalid_checkin,
                                                    update_booking_valid_token):
        for response2 in partial_update_booking_invalid_checkin:
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.patch(
                f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                json=partial_update_booking_invalid_checkin,
                headers={'Cookie': update_booking_valid_token})
            assert response2.status_code != 200, f"Wrong response code. Expected not 200, actual {response2.status_code} "

    '''↑🐞 Bag '''


    # невалидное поле checkout
    def test_partial_update_booking_invalid_checkout(self, update_booking_valid_data,
                                                    partial_update_booking_invalid_checkout,
                                                    update_booking_valid_token):
        for response2 in partial_update_booking_invalid_checkout:
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.patch(
                f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                json=partial_update_booking_invalid_checkout,
                headers={'Cookie': update_booking_valid_token})
            assert response2.status_code != 200, f"Wrong response code. Expected not 200, actual {response2.status_code} "

    '''↑🐞 Bag '''


    # невалидное поле additionalneeds
    def test_partial_update_booking_invalid_additionalneeds(self, update_booking_valid_data,
                                                     partial_update_booking_invalid_additionalneeds,
                                                     update_booking_valid_token):
        for response2 in partial_update_booking_invalid_additionalneeds:
            response1 = requests.post(url, json=update_booking_valid_data)
            response_as_dict = response1.json()
            response2 = requests.patch(f"https://restful-booker.herokuapp.com/booking/{response_as_dict['bookingid']}",
                                       json=partial_update_booking_invalid_additionalneeds,
                                       headers={'Cookie': update_booking_valid_token})
            assert response2.status_code != 200, f"Wrong response code. Expected not 200, actual {response2.status_code} "

    '''↑🐞 Bag '''

    # обновление по невалидному ID
    def test_partial_update_booking_invalid_id(self, partial_update_booking_valid_firstname, id_invalid_data,
                                               update_booking_valid_token):
        response = requests.put(f"https://restful-booker.herokuapp.com/booking/{id_invalid_data}",
                                json=partial_update_booking_valid_firstname,
                                headers={'Cookie': update_booking_valid_token})

        assert response.status_code == 400, "Update by invalid ID "

    # обновление по несуществующему ID
    def test_partial_update_booking_nonexistent_id(self, partial_update_booking_valid_firstname, id_nonexistent_data,
                                                   update_booking_valid_token):
        response = requests.put(f"https://restful-booker.herokuapp.com/booking/{id_nonexistent_data}",
                                json=partial_update_booking_valid_firstname,
                                headers={'Cookie': update_booking_valid_token})

        assert response.status_code == 400, "Update by non-existent ID "

