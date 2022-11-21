import pytest


class TestClass2:

    def test_case1(self, login):  # 调用了login
        print("TestClass1:test_case1")

    def test_case2(self):
        print("TestClass1:test_case2")


class TestClass3:
    def test_case1(self):
        print("TestClass2:test_case1")

    def test_case2(self, login):  # 调用了login
        print("TestClass2:test_case2")


@pytest.mark.usefixtures("login")  # TestClass3这个类，使用usefixtures调用了login
class TestClass4:
    @pytest.mark.usefixtures("login")
    def test_case1(self):
        print("TestClass3:test_case1")

    @pytest.mark.usefixtures("login")
    def test_case2(self):
        print("TestClass3:test_case2")



if __name__ == '__main__':
    pytest.main()