import pytest
import time


def testcase01():
    time.sleep(2)
    print('这里是testcase01')


def testcase02():
    time.sleep(3)
    print('这里是testcase02')


def testcase03():
    time.sleep(4)
    print('这里是testcase03')


def testcase04():
    time.sleep(5)
    print('这里是testcase04')


if __name__ == "__main__":
    pytest.main([__file__, '--workers=1', '--tests-per-worker=4'])
    # pytest.main(['-s',__file__,'-n=2'])
    # pytest.main(['-s',__file__])