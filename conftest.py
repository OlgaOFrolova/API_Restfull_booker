import pytest
import requests

@pytest.fixture
def auth_url():
    url = "https://restful-booker.herokuapp.com/auth"
    return (url)

@pytest.fixture
def booking_url():
    url = "https://restful-booker.herokuapp.com/booking/"
    return (url)


@pytest.fixture
def auth_pass():
    password = "password123"
    return (password)

@pytest.fixture
def auth_log():
    username = "admin"
    return (username)


@pytest.fixture
def negative_auth_admin_empty_login():
    username = [ None, "   ", ""]
    return (username)
@pytest.fixture
def negative_auth_admin_empty_pass():
    password = [ None, "   ", ""]
    return (password)

@pytest.fixture
def negative_swapped_login_pass():
        username = "password123"
        password = "admin"
        return {"username": username, "password": password}

@pytest.fixture
def negative_auth_admin_invalid_login():
    username = ["ADMIN", "AdMiN", None, "   ", "", "ad min", "   admin", "admin   ", "ad-min", "ad_min", "admin.",\
                "admin@", "фвьшт","約翰·史密斯", "존 스미스", "1", "12", 0, 123, 897, 123.87, -123, "!@#$%^&*", "☺☻♥♦♣♠•◘○", "password123"]
    return (username)

@pytest.fixture
def negative_auth_admin_invalid_pass():
    password = ["ADMIN", "AdMiN", None, "   ", "", "ad min", "   admin", "admin   ", "ad-min", "ad_min", "admin.",\
                "admin@", "фвьшт", "約翰·史密斯", "존 스미스","1", "12", 0, 123, 897, 123.87, -123, "!@#$%^&*", "☺☻♥♦♣♠•◘○", "admin"]
    return (password)

@pytest.fixture
def negative_firstmame():
    firstname = [" JOHN", "john", "JoHn", "SmiTh", None, "   ", "", "Ann Mary", "   John", "John   ", "Smith   ", "Ann-Mary",
                 "Smith-Wesson", "(John)", "Ощрт", "Иван", "約翰·史密斯", "존 스미스", "Jжон", "1", "12", 0, 123, 897, 123.87, -123,
                 "!@#$%^&*", "☺☻♥♦♣♠•◘○", "password123"]
    return (firstname)

@pytest.fixture
def negative_lastmame():
    lastname = ["SMITH", "smith", "SmiTh", None, "   ", "", "Smith Wesson", "   Smith", "Smith   ",
                "Smith-Wesson", "(Smith)", "Ыьшер", "фвьшт", "Сидоров", "約翰·史密斯", "존 스미스", "Sмит", "12", 0, 123,
                897, 123.87, -12, "!@#$%^&*", "☺☻♥♦♣♠•◘○", "password123"]
    return (lastname)

@pytest.fixture
def negative_checkin():
    checkin = [0, 10000000000000000000000000000000000, None, "   ", "", "2023-30-12", "2023- 31- 05", "2023 - 31 - 05",
              "0000-00-00", "0000-31-05", "2023-31-00", "2023-00-05", "2023-31-5", "02023-31-05", "9999-99-99",
              "9999-31-05", "2023-31-99", "2023-99-05", "2023-31-02", "2023-15-12", "2023-35-35", "2020-29-02",
              "2023-29-02", "2023-31-04" "-2023-12-12", "3000-12-12", "2023—05—23", "2023_05_23", "2023,05,23",
              "2023 05 23", "30.5.2006", "30-5-2006", "30/5/2006", "30.05.2006", " 30/05/2006", "5/30/2006", 1684866999,
              "Tue, 23 May 2023 18:36:38 GMT", "DATE(2023,05,23)", "23 мая 2023 года", "23 мая 2023г.",
              "23 May 2023", " £/$/%/&"]
    return(checkin)

@pytest.fixture
def negative_checkout():
    checkout = [0, 10000000000000000000000000000000000, None, "   ", "", "2023-30-12", "2023- 31- 05", "2023 - 31 - 05",
              "0000-00-00", "0000-31-05", "2023-31-00", "2023-00-05", "2023-31-5", "02023-31-05", "9999-99-99",
              "9999-31-05", "2023-31-99", "2023-99-05", "2023-31-02", "2023-15-12", "2023-35-35", "2020-29-02",
              "2023-29-02", "2023-31-04" "-2023-12-12", "3000-12-12", "2023—05—23", "2023_05_23", "2023,05,23",
              "2023 05 23", "30.5.2006", "30-5-2006", "30/5/2006", "30.05.2006", " 30/05/2006", "5/30/2006", 1684866999,
              "Tue, 23 May 2023 18:36:38 GMT", "DATE(2023,05,23)", "23 мая 2023 года", "23 мая 2023г.",
              "23 May 2023", " £/$/%/&"]
    return(checkout)

@pytest.fixture
def id_valid_data():
    id_valid_data = 123
    return id_valid_data


@pytest.fixture
def id_invalid_data():
    id_invalid_data = "abc"
    return id_invalid_data

@pytest.fixture
def id_nonexistent_data():
    id_nonexistent_data = 10000000000000000000000000000000000
    return id_nonexistent_data


@pytest.fixture
def create_firstname_valid_data():
    firstname = [ " ", "John", " JOHN", "john", "JoHn", "SmiTh",  "   ", "", "Ann Mary", "   John", \
            "John   ", "Smith   ", "Ann-Mary", "Smith-Wesson", "(John)", "Ощрт", "Иван", "約翰·史密斯", "존 스미스", "Jжон", \
            "1", "12", "!@#$%^&*", "☺☻♥♦♣♠•◘○", "password123"]
    return (firstname)

@pytest.fixture
def create_firstname_invalid_data():
    firstname = [ None,  123, 897, 123.87, -123]
    return (firstname)

@pytest.fixture
def create_lastname_valid_data():
    lastname = [" ", "John", " JOHN", "john", "JoHn", "SmiTh",  "   ", "", "Ann Mary", "   John", \
            "John   ", "Smith   ", "Ann-Mary", "Smith-Wesson", "(John)", "Ощрт", "Иван", "約翰·史密斯", "존 스미스", "Jжон", \
            "1", "12", "!@#$%^&*", "☺☻♥♦♣♠•◘○", "password123"]
    return (lastname)

@pytest.fixture
def create_lastname_invalid_data():
    lastname = [ None,  123, 897, 123.87, -123]
    return (lastname)

@pytest.fixture
def create_totalprice_valid_data():
    totalprice = [0, "   ", ""," %))))", 1000, 100.50, 100, 50, 100/50,
                  100 - 50, 10050, "пять тысяч рублей", "пять тысяч", "5 тысяч", "5000", "5000 pуб",
                  "five thousand dollars", "five thousand", " $ 5  thousand", " 5  thousand  $", " £/$/%/&", "оплачено"]
    return (totalprice)
@pytest.fixture
def create_totalprice_invalid_data():
    firstname = "John"
    lastname = "Smith"
    totalprice = None
    depositpaid = True
    bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
    additionalneeds = "Breakfast"

    return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
            "bookingdates": bookingdates, "additionalneeds": additionalneeds}

@pytest.fixture
def create_depositpaid_valid_data():
        firstname = "John"
        lastname = "Smith"
        totalprice = 100
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}

@pytest.fixture
def create_depositpaid_invalid_data():
    firstname = "John"
    lastname = "Smith"
    totalprice = 100
    depositpaid = None
    bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
    additionalneeds = "Breakfast"

    return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
            "bookingdates": bookingdates, "additionalneeds": additionalneeds}

@pytest.fixture
def create_checkin_valid_data():
    checkin = ["3000-12-12",  "2023,05,23", "2023 05 23", "5/30/2006", 1684866999,  "23 May 2023", "Tue, 23 May 2023 18:36:38 GMT",]
    return(checkin)

@pytest.fixture
def create_checkin_invalid_data():
    checkin = [10000000000000000000000000000000000, "   ", "","2023-30-12", "2023- 31- 05", "2023 - 31 - 05",
               "0000-00-00", "0000-31-05", "2023-31-00", "2023-00-05", "2023-31-5", "02023-31-05", "9999-99-99",
               "9999-31-05", "2023-31-99", "2023-99-05","2023-31-02", "2023-15-12","2023-35-35", "2020-29-02",
               "2023-29-02", "2023-31-04" "-2023-12-12",  "2023—05—23", "2023_05_23",  "30.5.2006", "30-5-2006",
               "30/5/2006", "30.05.2006", " 30/05/2006",  "DATE(2023,05,23)",
               "23 мая 2023 года", "23 мая 2023г.", " £/$/%/&"]
    return(checkin)

@pytest.fixture
def create_checkin_none_data():
    checkin = [None]
    return (checkin)

@pytest.fixture
def create_checkout_valid_data():
    checkout = ["3000-12-12",  "2023,05,23", "2023 05 23", "5/30/2006", 1684866999,  "23 May 2023", "Tue, 23 May 2023 18:36:38 GMT",]
    return(checkout)

@pytest.fixture
def create_checkout_invalid_data():
    checkout = [10000000000000000000000000000000000, "   ", "","2023-30-12", "2023- 31- 05", "2023 - 31 - 05",
               "0000-00-00", "0000-31-05", "2023-31-00", "2023-00-05", "2023-31-5", "02023-31-05", "9999-99-99",
               "9999-31-05", "2023-31-99", "2023-99-05","2023-31-02", "2023-15-12","2023-35-35", "2020-29-02",
               "2023-29-02", "2023-31-04" "-2023-12-12",  "2023—05—23", "2023_05_23",  "30.5.2006", "30-5-2006",
               "30/5/2006", "30.05.2006", " 30/05/2006",  "DATE(2023,05,23)",
               "23 мая 2023 года", "23 мая 2023г.", " £/$/%/&"]
    return(checkout)

@pytest.fixture
def create_checkout_none_data():
    checkout = [None]
    return (checkout)



@pytest.fixture
def create_additionalneeds_valid_data():
    additionalneeds = ["breakfast", None, "   ", "","BREAKFAST", "BrEaKfAsT", "break fast", "   breakfast"," breakfast   ",
                       " break-fast","( breakfast)", "икуфлафые", "завтрак","1", "12", 0, 123, 897, 123.87, -123,
                       "!@#$%^&*", "☺☻♥♦♣♠•◘○","約翰·史密斯", "존 스미스"]

    return (additionalneeds)




@pytest.fixture
def update_booking_valid_data():
    update_booking_valid_data = {
        "firstname": "Igor",
        "lastname": "Petrov",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-03-10",
            "checkout": "2023-03-20"},
        "additionalneeds": "Breakfast"
    }
    return (update_booking_valid_data)


@pytest.fixture
def update_booking_new_valid_data():
    update_booking_new_valid_data = {
        "firstname": "Petr",
        "lastname": "Petrov",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-03-10",
            "checkout": "2023-03-20"},
        "additionalneeds": "Breakfast"
    }
    return (update_booking_new_valid_data)


@pytest.fixture
def update_booking_all_valid_data():
    update_booking_all_valid_data = {
        "firstname": "Petr",
        "lastname": "Petrov",
        "totalprice": 5000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-03-10",
            "checkout": "2025-03-20"},
        "additionalneeds": "Sea view"
    }
    return (update_booking_all_valid_data)


@pytest.fixture
def update_booking_valid_token():
    data_auth = {"username": "admin",
                 "password": "password123"}
    response = requests.post("https://restful-booker.herokuapp.com/auth", data=data_auth)
    token_auth = "token=" + (response.json()['token'])
    return (token_auth)


@pytest.fixture
def update_booking_invalid_token():
    data_auth = {"username": "admin",
                 "password": "password123"}
    response = requests.post("https://restful-booker.herokuapp.com/auth", data=data_auth)
    token_auth = "token=" + (response.json()['token'] + '1')
    return (token_auth)


@pytest.fixture
def update_booking_valid_authorization_header():
    valid_authorization_header = {'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}
    return (valid_authorization_header)


@pytest.fixture
def update_booking_invalid_authorization_header():
    invalid_authorization_header = {'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=007'}
    return (invalid_authorization_header)


@pytest.fixture
def partial_update_booking_valid_firstname():
    partial_update_booking_valid_firstname = {"firstname": "Petr"}
    return (partial_update_booking_valid_firstname)


@pytest.fixture
def partial_update_booking_valid_lastname():
    partial_update_booking_valid_lastname = {"lastname": "Sidoroff"}
    return (partial_update_booking_valid_lastname)


@pytest.fixture
def partial_update_booking_valid_totalprice():
    partial_update_booking_valid_totalprice = {"totalprice": 7000}
    return (partial_update_booking_valid_totalprice)


@pytest.fixture
def partial_update_booking_valid_depositpaid():
    partial_update_booking_valid_depositpaid = {"depositpaid": False}
    return (partial_update_booking_valid_depositpaid)


@pytest.fixture
def partial_update_booking_valid_checkin():
    partial_update_booking_valid_checkin = {"bookingdates": {"checkin": "2025-03-07"}}
    return (partial_update_booking_valid_checkin)


@pytest.fixture
def partial_update_booking_valid_checkout():
    partial_update_booking_valid_checkout = {"bookingdates": {"checkout": "2025-03-08"}}
    return (partial_update_booking_valid_checkout)


@pytest.fixture
def partial_update_booking_valid_additionalneeds():
    partial_update_booking_valid_additionalneeds = {"additionalneeds": "Sea view"}
    return (partial_update_booking_valid_additionalneeds)


@pytest.fixture
def partial_update_booking_invalid_firstname():
    partial_update_booking_invalid_firstname = [{"firstname": None}, {"firstname": 5}, {"firstname": 5.5},
                                                {"firstname": {'name': 'name'}}, {"firstname": ['name1', 'name2']},
                                                {"firstname": True}]
    return (partial_update_booking_invalid_firstname)


@pytest.fixture
def partial_update_booking_invalid_lastname():
    partial_update_booking_invalid_lastname = [{"lastname": None}, {"lastname": 5}, {"lastname": 5.5},
                                               {"lastname": {'name': 'name'}}, {"lastname": ['name1', 'name2']},
                                               {"lastname": True}]
    return (partial_update_booking_invalid_lastname)


@pytest.fixture
def partial_update_booking_invalid_totalprice():
    partial_update_booking_invalid_totalprice = [{"totalprice": None}, {"totalprice": "John"}, {"totalprice": 5.5},
                                               {"totalprice": {'name': 'name'}}, {"totalprice": ['name1', 'name2']},
                                               {"totalprice": True}]
    return (partial_update_booking_invalid_totalprice)


@pytest.fixture
def partial_update_booking_invalid_depositpaid():
    partial_update_booking_invalid_depositpaid = [{"depositpaid": None}, {"depositpaid": "John"}, {"depositpaid": 5.5},
                                                  {"depositpaid": {'name': 'name'}}, {"depositpaid": ['name1', 'name2']},
                                                  {"depositpaid": 108}]
    return (partial_update_booking_invalid_depositpaid)


@pytest.fixture
def partial_update_booking_invalid_checkin():
    partial_update_booking_invalid_checkin = [{"bookingdates":{"checkin": None}},
                                              {"bookingdates":{"checkin": "John"}},
                                              {"bookingdates":{"checkin": 5.5}},
                                              {"bookingdates":{"checkin": {'name': 'name'}}},
                                              {"bookingdates":{"checkin": ['name1', 'name2']}},
                                              {"bookingdates":{"checkin": True}}]
    return (partial_update_booking_invalid_checkin)


@pytest.fixture
def partial_update_booking_invalid_checkout():
    partial_update_booking_invalid_checkout = [{"bookingdates":{"checkout": None}},
                                              {"bookingdates":{"checkout": "John"}},
                                              {"bookingdates":{"checkout": 5.5}},
                                              {"bookingdates":{"checkout": {'name': 'name'}}},
                                              {"bookingdates":{"checkout": ['name1', 'name2']}},
                                              {"bookingdates":{"checkout": True}}]
    return (partial_update_booking_invalid_checkout)

@pytest.fixture
def partial_update_booking_invalid_additionalneeds():
    partial_update_booking_invalid_additionalneeds = [{"firstname": None}, {"firstname": 5}, {"firstname": 5.5},
                                                {"firstname": {'name': 'name'}}, {"firstname": ['name1', 'name2']},
                                                {"firstname": True}]
    return (partial_update_booking_invalid_additionalneeds)

