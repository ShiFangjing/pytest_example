import pytest


@pytest.fixture(scope='class')  # 名为login的fixture，完成登陆和注册操作
def login():
    print('class'+'登录操作')
    yield
    print('class'+'注销操作')
