import pytest
from step_use.common_function import login


@pytest.fixture(scope="session")
def login_setup():
    login("shi", "123456")
