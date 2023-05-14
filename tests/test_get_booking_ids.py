import requests
import json

class TestBookingIds:

    # возврат идентификаторов всех бронирований
    def test_check_all_id(self):
        url = f'https://restful-booker.herokuapp.com/booking/'
        response = requests.get(url)
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
    def test_check_invalid_firstname(self):
        for firstname in "##$@@", 108, 5.5, {"name": "name"}, ["name1", "name2"], True:
            url = f"https://restful-booker.herokuapp.com/booking?firstname={firstname}"
            response = requests.get(url)
            assert not response.json(), f"The firstname {firstname}is invalid, but it is in the results"

    # пустое поле firstname
    def test_check_empty_firstname(self):
        firstname = " "
        url = f"https://restful-booker.herokuapp.com/booking?firstname={firstname}"
        response = requests.get(url)
        assert not response.json(), f"The firstname is empty, but it is in the results"


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
    def test_check_invalid_lastname(self):
        for lastname in "##$@@", 108, 5.5, {"name": "name"}, ["name1", "name2"], True:
            url = f"https://restful-booker.herokuapp.com/booking?lastname={lastname}"
            response = requests.get(url)
            assert not response.json(), f"The lastname {lastname}is invalid, but it is in the results"

    # пустое поле lastname
    def test_check_empty_lastname(self):
        lastname = " "
        url = f"https://restful-booker.herokuapp.com/booking?lastname={lastname}"
        response = requests.get(url)
        assert not response.json(), f"The lastname is empty, but it is in the results"

    # возврат списка пользователей по полю «checkin»

    # формат CCYY-MM-DD
    def test_check_valid_checkin(self):
        checkin = "2015-05-15"
        url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
        response = requests.get(url)
        assert response.json(), "No checkin result"

    # невалидный формат даты
    def test_check_invalid_checkin(self):
        for checkin in "15-05-2015", "##$@@", 108, 5.5, {"name": "name"}, ["name1", "name2"], True:
            try:
                url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
                response = requests.get(url)
            except requests.exceptions.JSONDecodeError:
                assert not response.json(),"Checkin invalid date format"

    # дата заезда выходит за диапазон предусмотренных значений
    def test_check_out_of_range_checkin(self):
        checkin = "3000-05-15"
        try:
            url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
            response = requests.get(url)
        except requests.exceptions.JSONDecodeError:
            assert not response.json(), "Checkin date is out of range"

    # пустое поле даты
    def test_check_empty_checkin(self):
        checkin = " "
        try:
            url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
            response = requests.get(url)
        except requests.exceptions.JSONDecodeError:
            assert not response.json(), "Checkin date is empty"


    # возврат списка пользователей по полю «checkout»

    # формат CCYY-MM-DD
    def test_check_valid_checkout(self):
        checkout = "2015-05-15"
        url = f"https://restful-booker.herokuapp.com/booking?checkout={checkout}"
        response = requests.get(url)
        assert response.json(), "No checkout result"

    # невалидный формат даты
    def test_check_invalid_checkout(self):
        for checkout in "15-05-2015", "##$@@", 108, 5.5, {"name": "name"}, ["name1", "name2"], True:
            try:
                url = f"https://restful-booker.herokuapp.com/booking?checkout={checkout}"
                response = requests.get(url)
            except requests.exceptions.JSONDecodeError:
                assert not response.json(), "checkout invalid date format"


    # дата выезда выходит за диапазон предусмотренных значений
    def test_check_out_of_range_checkout(self):
        checkout = "3000-05-15"
        try:
            url = f"https://restful-booker.herokuapp.com/booking?checkout={checkout}"
            response = requests.get(url)
        except requests.exceptions.JSONDecodeError:
            assert not response.json(), "Checkout date is out of range"

    # пустое поле даты
    def test_check_empty_checkout(self):
        checkout = " "
        try:
            url = f"https://restful-booker.herokuapp.com/booking?checkout={checkout}"
            response = requests.get(url)
        except requests.exceptions.JSONDecodeError:
            assert not response.json(), "Checkout date is empty"

    # python -m pytest tests/test_get_booking_ids.py
