import pytest
import allure
from .common_function2 import *


class TestStep:
    """@allure.step()方式实现step，测试报告可以显示参数"""

    @allure.feature("功能模块")
    @allure.story("测试用例小模块-成功案例")
    @allure.title("第二种实现方式：流程性的用例，添加测试步骤")
    def test_add_goods_and_buy_2(login_setup):
        '''
        用例描述：
        前置：登陆
        用例步骤：1.浏览商品 2.添加购物车  3.购买  4.支付成功
        '''
        open_goods()
        add_shopping_cart(goods_id="10086")
        buy_goods()
        pay_goods()
        assert 1 == 1

# Terminal运行两条命令生成allure测试报告
# pytest --alluredir allure_report test_step2.py --clean-alluredir
# allure serve allure_report
