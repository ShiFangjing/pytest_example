import functools


def outer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"before...")
        func(*args, **kwargs)
        print("after...")

    return inner


@outer
def add(a, b):
    """
    求和运算
    """
    print(a + b)


add(10, 11)
