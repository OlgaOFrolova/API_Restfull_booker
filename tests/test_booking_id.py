import requests

class TestBookingId:
    #ввод валидного ID
    def test_check_valid_id(self):
        data = 569
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        assert response.status_code == 200, "Wrong status code for valid ID"

    # ввод ID = 0
    def test_check_zero_id(self):
        data = 0
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        assert response.status_code == 404, "ID = 0"

    # ввод несуществующего ID(большое число)
    def test_check_big_id(self):
        data = 100000000000000000000000000000000000000000
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        assert response.status_code == 404, "ID greater than range "

    # ввод несуществующего ID(буквы, спецсимволы, float и т.д)
    def test_check_invalid_id(self):
        for data in "abc", "##$@@",  5.5 , {"name": "name"}, ["name1", "name2"], True:
            url = f'https://restful-booker.herokuapp.com/booking/{{"name": "name"}}'
            response = requests.get(url)
            assert response.status_code == 404, "Invalid ID"

    # ввод пустого ID
    def test_check_empty_id(self):
        data = " "
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        assert response.status_code == 404, "Empty ID"

    # время ответа
    def test_check_time(self):
         data = 123
         url = f'https://restful-booker.herokuapp.com/booking/{data}'
         response = requests.get(url)
         assert response.elapsed.total_seconds() <= 1, "Response time is more than 1s"

    # в ответе существуют определенные json-поля
    def test_check_body_text(self):

        data = 569
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        response2 = response.content.decode("utf-8")
        assert "firstname" in response2, "Not firstname in response "
        assert "lastname" in response2, "Not lastname in response "
        assert "totalprice" in response2, "Not totalprice in response "
        assert "depositpaid" in response2, "Not depositpaid in response "
        assert "checkin" in response2, "Not checkin in response "
        assert "checkout" in response2, "Not checkout in response "

    #  ответ возвращает определенные значения
    def test_check_response_data(self):
        data = 568
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        response_as_dict = response.json()

        assert response_as_dict['firstname'] =="John",  "Wrong firstname  in response "
        assert response_as_dict['lastname'] == "Allen", "Wrong lastname  in response "
        assert response_as_dict['totalprice'] == 111, "Deposit not paid in response "
        assert response_as_dict['depositpaid'] == True,  "Deposit not paid in response "
        assert response_as_dict['bookingdates']["checkin"] == "2018-01-01", "Not booking checkin dates "
        assert response_as_dict['bookingdates']["checkout"] == "2019-01-01", "Not booking checkout dates "
        assert response_as_dict['additionalneeds'] == "super bowls", "Not additional needs "

    # значение totalprice больше или меньше определенного числа
    def test_check_compare_data(self):
        data = 569
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        response_as_dict = response.json()
        assert response_as_dict['totalprice'] > 100,  "Total price less than 100 "

    # проверка формата полей
    def test_check_response_format(self):
        data = 569
        url = f'https://restful-booker.herokuapp.com/booking/{data}'
        response = requests.get(url)
        response_as_dict = response.json()

        assert isinstance(response_as_dict['firstname'], str), f'field {response_as_dict["firstname"]} not of String format'
        assert isinstance(response_as_dict['lastname'], str), f'field {response_as_dict["lastname"]} not of String format'
        assert isinstance(response_as_dict['additionalneeds'], str), f'field {response_as_dict["additionalneeds"]} not of String format'
        assert isinstance(response_as_dict['totalprice'], int), f'field {response_as_dict["totalprice"]} not of Integer format'
        assert isinstance(response_as_dict['depositpaid'], bool), f'field {response_as_dict["depositpaid"]} not of Boolean format'
        assert isinstance(response_as_dict['bookingdates']["checkin"],  str), f'field {["bookingdates"]["checkin"]} not of data format'
        assert isinstance(response_as_dict['bookingdates']["checkout"], str), f'field {["bookingdates"]["checkout"]} not of data format'
