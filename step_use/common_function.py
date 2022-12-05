'''
流程性的用例，添加测试步骤，让用例更清晰
用例步骤：1.登陆， 2.浏览商品 3.添加购物车  4.生成订单  5.支付成功
'''


def login(username, password):
    '''登陆'''
    print("前置操作：先登陆")


def open_goods():
    '''浏览商品'''
    print("浏览商品")


def add_shopping_cart(goods_id="10086"):
    '''添加购物车'''
    print("添加购物车")


def buy_goods():
    '''生成订单'''
    print("buy")


def pay_goods():
    '''支付'''
    print("pay")
