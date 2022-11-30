class TestCache(object):
    def test_1(self, cache, create_id):
        # 方式1：cache获取
        get_id = cache.get("id", None)
        print("获取到的id: {}".format(get_id))
        print("create_id fixture return: {}".format(create_id))
        assert get_id == create_id
