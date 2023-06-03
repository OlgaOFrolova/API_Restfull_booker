import requests

class TestBookingIds:

    # возврат идентификаторов всех бронирований
    def test_check_all_id(self, booking_url):
        response = requests.get(booking_url)
        assert response.json(), "No booking result"


    # возврат списка пользователей по полю «firstname»
    # валидное имя, которое есть в базе
    def test_check_valid_firstname(self):
        firstname = "John"
        url = f"https://restful-booker.herokuapp.com/booking?firstname={firstname}"
        response = requests.get(url)
        assert response.json(), "No firstname result"

    # валидное имя, которого нет в базе
    def test_check_valid_firstname_not_in_base(self):
        firstname = "Rumplestiltskin"
        url = f"https://restful-booker.herokuapp.com/booking?firstname={firstname}"
        response = requests.get(url)
        assert not response.json(), f"The firstname {firstname}is not in the database, but it is in the results"


    # невалидное имя
    def test_check_invalid_firstname(self, create_firstname_invalid_data):
        for firstname in create_firstname_invalid_data:
            url = f"https://restful-booker.herokuapp.com/booking?firstname={firstname}"
            response = requests.get(url)
            assert not response.json(), f"The firstname {firstname}is invalid, but it is in the results"


    # возврат списка пользователей по полю «lastname»
    # валидная фамилия, которая есть в базе
    def test_check_valid_lastname(self):
        lastname = "Smith"
        url = f"https://restful-booker.herokuapp.com/booking?lastname={lastname}"
        response = requests.get(url)
        assert response.json(), "No lastname result"

    # валидная фамилия, которой нет в базе
    def test_check_valid_lastname_not_in_base(self):
        lastname = "Rumplestiltskin108"
        url = f"https://restful-booker.herokuapp.com/booking?lastname={lastname}"
        response = requests.get(url)
        assert not response.json(), f"The lastname {lastname} is not in the database, but it is in the results"

    # невалидная фамилия
    def test_check_invalid_lastname(self, create_lastname_invalid_data):
        for lastname in create_lastname_invalid_data:
            url = f"https://restful-booker.herokuapp.com/booking?firstname={lastname}"
            response = requests.get(url)
            assert not response.json(), f"The lastname {lastname}is invalid, but it is in the results"

    # возврат списка пользователей по полю «checkin»
    # формат CCYY-MM-DD
    def test_check_valid_checkin(self):
        checkin = "2015-05-15"
        url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
        response = requests.get(url)
        assert response.json(), "No checkin result"

    # невалидный формат даты
    def test_check_invalid_checkin(self, create_checkin_invalid_data):
        for checkin in create_checkin_invalid_data:
                url = f"https://restful-booker.herokuapp.com/booking?firstname={checkin}"
                response = requests.get(url)
                assert not response.json(), f"Checkin {checkin}is invalid, but it is in the results"


    # возврат списка пользователей по полю «checkout»
    # формат CCYY-MM-DD
    def test_check_valid_checkout(self):
        checkout = "2023-05-05"
        url = f"https://restful-booker.herokuapp.com/booking?checkout={checkout}"
        response = requests.get(url)
        assert response.json(), "No checkout result"

    # невалидный формат даты
    def test_check_invalid_checkout(self, create_checkout_invalid_data):
        for checkout in create_checkout_invalid_data:
            url = f"https://restful-booker.herokuapp.com/booking?firstname={checkout}"
            response = requests.get(url)
            assert not response.json(), f"Checkin {checkout}is invalid, but it is in the results"
