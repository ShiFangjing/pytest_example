import allure


@allure.step("setup:登陆")
def login(username, password):
    '''登陆'''
    print("前置操作：先登陆")


@allure.step("step:浏览商品")
def open_goods():
    '''浏览商品'''
    print("浏览商品")


@allure.step("step:添加购物车")
def add_shopping_cart(goods_id="10086"):
    '''添加购物车'''
    print("添加购物车")


@allure.step("step:生成订单")
def buy_goods():
    '''生成订单'''
    print("buy")


@allure.step("step:支付")
def pay_goods():
    '''支付'''
    print("pay")
