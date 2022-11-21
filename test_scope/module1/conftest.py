import pytest


@pytest.fixture()
def login():
    print('function' + '登录操作')
    yield
    print('function' + '注销操作')
