#coding=utf-8


class BaseProxyPolicy(object):
    """proxy policy base, define basic interface;
    """

    def __init__(self, name):
        self.name = name

    def update(self, *argv, **kw):
        pass

    def getProxy(self, spider, request):
        pass

    def updateStatus(self, proxy, status, *argv, **kw):
        pass


class RandomProxyPolicy(BaseProxyPolicy):
    """get random proxy
    """
    from random import sample

    def __init__(self):
        super(RandomProxyPolicy, self).__init__(self, "random_proxy_policy")
        # proxy -> proxy model
        self._pool = {}

    def update(self, *argv, **kw):
        pass

    def getProxy(self, spider, request):
        sample(self._pool.items(), 1)[0]

    def updateStatus(self, proxy, cralw_status, *argv, **kw):
        pass
