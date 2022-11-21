import pytest


@pytest.mark.usefixtures("login")
class TestClass1:
    def test_case1(self):
        print("TestClass1:test_case1")

    def test_case2(self):
        print("TestClass1:test_case2")


class TestClass2:
    def test_case1(self):
        print("TestClass2:test_case1")

    def test_case2(self):
        print("TestClass2:test_case2")


if __name__ == '__main__':
    pytest.main()