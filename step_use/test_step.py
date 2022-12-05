import pytest
import allure
from .common_function import *


class TestStep:
    """with方式实现step，代码更整洁，但是测试报告不显示step的参数"""

    @allure.feature("功能模块")
    @allure.story("测试用例小模块-成功案例")
    @allure.title("测试用例名称：流程性的用例，添加测试步骤")
    def test_add_goods_and_buy(login_setup):
        '''
        用例描述：
        前置：登陆
        用例步骤：1.浏览商品 2.添加购物车  3.购买  4.支付成功
        '''
        with allure.step("step1：浏览商品"):
            open_goods()

        with allure.step("step2：添加购物车"):
            add_shopping_cart()

        with allure.step("step3：生成订单"):
            buy_goods()

        with allure.step("step4：支付"):
            pay_goods()

        with allure.step("断言"):
            assert 1 == 1

# Terminal运行两条命令生成allure测试报告
# pytest --alluredir allure_report test_step.py --clean-alluredir
# allure serve allure_report
