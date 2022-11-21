import pytest


@pytest.fixture(scope='module')  # 名为login的fixture，完成登陆和注册操作
def login():
    print('module'+'登陆操作')
    yield
    print('module'+'注销操作')
