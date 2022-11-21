import pytest


@pytest.fixture(scope='session', autouse=True)  # 名为login的fixture，完成登陆和注册操作
def login():
    print('session'+'登录操作')
    yield
    print('session'+'注销操作')
