#coding=utf-8




class _BaseFetcher(object):

    """基本抓取器
    get_result      得到链接网页信息
    """

    def __init__(self):
        pass

    def request(self, urls, method='get', *argv, **kw):
        raise NotImplementedError


from grequests import request


class BaseFetcher(object):

    def request(self, urls, method='get', *argv, **kw):
        if urls:
            if isinstance(urls, str):
                yield request(method, urls, **kw).send()
            elif isinstance(urls, (tuple, list)):
                reqs = [request(method, url, **kw) for url in urls]
                yield imap(request, stream=kw['stream'] if kw.has_key('stream') else False)
        else:
            raise ValueError

