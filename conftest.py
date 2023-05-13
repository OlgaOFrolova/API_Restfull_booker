import pytest


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
