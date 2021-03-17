import pytest
from utils.login import Login

@pytest.fixture(scope="session")
def GetHeader():
    res = Login().change_company_and_login()
    if res.json()["code"] == 200:
        headers = Login().get_headers()
        headers["token"] = Login.token
    return headers

def pytest_configure(config):
    config.addinivalue_line(
        "markers","smoke"
    )