import pytest_mock


def add(a, b):
    return a + b


# 使用mock的return_value参数改变add返回的数据
@pytest_mock.pytest_addoption('add', return_value=10)
def test_add():
    print(add(1, 2))  # 10
