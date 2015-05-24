# coding=utf-8


class BaseFetcher(object):
    """基本抓取器
    get_result      得到链接网页信息
    """

    def __init__(self):
        pass

    def get_result(self, urls, *argv, **kw):
        raise NotImplementedError
