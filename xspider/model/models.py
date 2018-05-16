#coding=utf-8
from fileds import Fileds
import time
import json
from xspider.libs import page_util


class ZRequest(object):
    """抓取请求
    """
    __attr__ = [
        "url", "pre_url", "method", "params", "headers", "dir_path",
        "retry_count", "last_crawl"
    ]

    def __init__(self, url, pre_url, dir_path, *argv, **kw):
        super(ZRequest, self).__init__()
        self.url = url
        self.pre_url = pre_url
        self.method = kw.get("method", "GET").lower()
        self.params = kw.get("params", {})
        self.headers = kw.get(
            "headers", {
                'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
            })
        self.dir_path = dir_path + 1
        self.retry_count = kw.get("retry_count", 3)
        self.last_crawl = None
        self.timeout = kw.get("timeout", None)

    def dumps(self):
        return json.dumps(
            {attr: getattr(self, attr)
             for attr in self.__attr__})

    @staticmethod
    def loads(value):
        """通过字符串加载对象，通过字符串序列化
            param:value:basestring:反序列化字符串
            return:ZRequest:ZRequest:返回反序列化对象
            Test:
                >>> request = ZRequest("www.baidu.com","pre",0)
                >>> j = request.dumps()
                >>> r = ZRequest.loads(j)
                {"url": "www.baidu.com", "headers": {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}, "params": {}, "method": "get", "dir_path": 2}
        """
        d = json.loads(value)
        url = d["url"]
        dir_path = d["dir_path"]
        pre_url = d["pre_url"]
        del d["url"]
        del d["dir_path"]
        del d["pre_url"]
        return ZRequest(url, pre_url, dir_path, **d)


class ZResponse(object):
    """网页抓取返回结果

        Test:
            >>> response = ZResponse("x","j",raw_text = "abc")
            >>> response.encoding = "utf-8"
            >>> response.text
            'abc'
    """
    __attr__ = ["redirect_url", "url", "status_code"]

    def __init__(self, url, pre_url, *argv, **kw):
        super(ZResponse, self).__init__()
        self.redirect_url = kw.get("redirect_url", url)
        self.url = url
        self.request = kw.get("request", ZRequest(url, pre_url, -1))
        self.status_code = kw.get("status_code", -1)
        self.raw_text = kw.get("raw_text", None)
        self.headers = kw.get("header", {})
        self.crawl_time = kw.get("crawl_time", time.time())
        self.error = kw.get("error", None)
        self.cost = kw.get("cost_time", None)
        self._charset = None
        self._text = None
        self.encoding = kw.get("encoding", None)

    def __str__(self):
        return json.dumps(
            {attr: getattr(self, attr)
             for attr in self.__attr__})

    @property
    def charset(self):
        if self._charset is None and self.raw_text is not None:
            self._charset = page_util.get_html_charset(bytes(self.raw_text))
        return self._charset

    @property
    def text(self):
        encoding = self.encoding
        if encoding is None:
            return self.raw_text
        if self.raw_text is None:
            return None
        if self._text is None:
            if self.encoding != self.charset:
                self._text = self.raw_text.decode(self.charset).encode(
                    self.encoding)
            else:
                self._text = self.raw_text
        return self._text


class ProxyInfo(object):
    """代理配置
        eg. http://user:pass@10.10.1.10:3128/'
    """

    def __init__(self,
                 protocal='http',
                 user=None,
                 passwd=None,
                 host=None,
                 port=None):
        self.protocal = protocal
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port

    def __rep__(self):
        host = "{}:{}".format(self.host, self.port) if self.port else self.host
        us = "{}:{}@".format(self.user, self.passwd) if self.user else ""
        return "{protocal}://{user}{host}/".format(
            protocal=self.protocal, user=user, host=host)
