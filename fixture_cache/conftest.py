import pytest


@pytest.fixture()
def create_id(cache):
    """取值生成一个id"""
    id = "shi_10086"
    cache.set("id", id)
    yield id