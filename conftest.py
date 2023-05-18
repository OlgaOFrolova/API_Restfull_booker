import pytest
import requests


@pytest.fixture
def auth_positive():
    username = "admin"
    password = "password123"
    return {"username": username, "password": password}


@pytest.fixture
def auth_negative_register_login():
    username = "ADMIN"
    password = "password123"
    return {"username": username, "password": password}


@pytest.fixture
def auth_negative_register_pass():
    username = "admin"
    password = "PASSWORD!@#"
    return {"username": username, "password": password}


@pytest.fixture
def auth_admin_wrong_pass():
    username = "admin"
    password = "987654321"
    return {"username": username, "password": password}


@pytest.fixture
def auth_admin_wrong_login():
    username = "admin123"
    password = "password123"
    return {"username": username, "password": password}


@pytest.fixture
def auth_admin_wrong_login_pass():
    username = "admin123"
    password = "987654321"
    return {"username": username, "password": password}


@pytest.fixture
def auth_admin_empty_login():
    username = " "
    password = "password123"
    return {"username": username, "password": password}


@pytest.fixture
def auth_admin_empty_pass():
    username = "admin"
    password = " "
    return {"username": username, "password": password}


@pytest.fixture
def auth_admin_empty_login_pass():
    username = " "
    password = " "
    return {"username": username, "password": password}


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
    for firstname in " ", "John":
        firstname = firstname
        lastname = "Smith"
        totalprice = 1000
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_lastname_valid_data():
    for lastname in " ", "Smith":
        firstname = "John"
        lastname = lastname
        totalprice = 1000
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_totalprice_valid_data():
    for totalprice in " ", "Price", 5, 5.5, {'name': 'name'}, ['name1', 'name2'], True:
        firstname = "John"
        lastname = "Smith"
        totalprice = totalprice
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_depositpaid_valid_data():
    for depositpaid in " ", "Price", 5, 5.5, {'name': 'name'}, ['name1', 'name2'], True:
        firstname = "John"
        lastname = "Smith"
        totalprice = 100
        depositpaid = depositpaid
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_checkin_valid_data():
    for checkin in " ", "Price", 5, 5.5, {'name': 'name'}, ['name1', 'name2'], True:
        firstname = "John"
        lastname = "Smith"
        totalprice = 100
        depositpaid = True
        bookingdates = {"checkin": checkin, "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_checkout_valid_data():
    for checkout in " ", "Price", 5, 5.5, {'name': 'name'}, ['name1', 'name2'], True:
        firstname = "John"
        lastname = "Smith"
        totalprice = 100
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": checkout}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_additionalneeds_valid_data():
    for additionalneeds in " ", "Price", 5, 5.5, {'name': 'name'}, ['name1', 'name2'], True:
        firstname = "John"
        lastname = "Smith"
        totalprice = 100
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = additionalneeds

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_booking_invalid_firstname_data():
    for firstname in None, 5, 5.5, {'name': 'name'}, ['name1', 'name2'], True:
        firstname = firstname
        lastname = "Smith"
        totalprice = 1000
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_booking_invalid_lastname_data():
    for lastname in None, 5, 5.5, {'name': 'name'}, ['name1', 'name2'], True:
        firstname = "John"
        lastname = lastname
        totalprice = 1000
        depositpaid = True
        bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
        additionalneeds = "Breakfast"

        return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_booking_invalid_totalprice_data():
    firstname = "John"
    lastname = "Smith"
    totalprice = None
    depositpaid = True
    bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
    additionalneeds = "Breakfast"

    return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
            "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_booking_invalid_depositpaid_data():
    firstname = "John"
    lastname = "Smith"
    totalprice = 100
    depositpaid = None
    bookingdates = {"checkin": "2023-03-10", "checkout": "2023-03-20"}
    additionalneeds = "Breakfast"

    return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
            "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_booking_invalid_checkin_data():
    firstname = "John"
    lastname = "Smith"
    totalprice = 100
    depositpaid = None
    bookingdates = {"checkin": None, "checkout": "2023-03-20"}
    additionalneeds = "Breakfast"

    return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
            "bookingdates": bookingdates, "additionalneeds": additionalneeds}


@pytest.fixture
def create_booking_invalid_checkout_data():
    firstname = "John"
    lastname = "Smith"
    totalprice = 100
    depositpaid = None
    bookingdates = {"checkin": "2023-03-10", "checkout": None}
    additionalneeds = "Breakfast"

    return {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
            "bookingdates": bookingdates, "additionalneeds": additionalneeds}


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