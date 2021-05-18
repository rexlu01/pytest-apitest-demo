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

def pytest_collection_modifyitems(items):
    """
    pytest.mark.parametrize对用例进行参数化时，传入的值中包括汉字，运行用例时，控制台显示的参数存在编码问题
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_sessionstart(session):
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        item.session.results[item] = result

def pytest_sessionfinish(session, exitstatus):
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    total_amout = passed_amount + failed_amount
    pass_rate = "0.00%"
    if total_amout > 0:
        pass_rate = str("%.2f%%" % (float(passed_amount) / float(total_amout) * 100))
    message = f"接口通过： {passed_amount}, 接口失败： {failed_amount}, 接口通过率；{pass_rate}"
    result_message = f"{message}\n"
    if passed_amount:
        with open("." + os.sep + "resultAPI.txt", "w+", encoding="utf8") as f:
            f.seek(0)
            f.truncate()
            f.write(result_message)