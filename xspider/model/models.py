#coding=utf-8
from fileds import Fileds
import time
import json


class ZRequest(Fileds):
    """抓取请求
    """

    def __init__(self, url, pre_url, dir_path, *argv, **kw):
        super(ZRequest, self).__init__(*argv, **kw)
        self["url"] = url
        self["pre_url"] = pre_url
        self["method"] = kw.get("method", "GET").lower()
        self["params"] = kw.get("params", {})
        self["headers"] = kw.get(
            "headers", {
                'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
            })
        self["coding"] = kw.get("fetch_coding", None)
        self["dir_path"] = dir_path + 1
        self["retry_count"] = kw.get("retry_count", 3)
        self["last_crawl"] = None

    def dumps(self):
        return json.dumps(self)

    @staticmethod
    def loads(value):
        """通过字符串加载对象，通过字符串序列化
            param:value:basestring:反序列化字符串
            return:ZRequest:ZRequest:返回反序列化对象
            Test:
                >>> request = ZRequest("www.baidu.com",0)
                >>> j = request.dumps()
                >>> r = ZRequest.loads(j)
                >>> print r
                {"url": "www.baidu.com", "headers": {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}, "params": {}, "method": "get", "dir_path": 2}
        """
        d = json.loads(value)
        url = d["url"]
        dir_path = d["dir_path"]
        del d["url"]
        del d["dir_path"]
        return ZRequest(url, dir_path, **d)


class ZResponse(Fileds):
    def __init__(self, url, pre_url, *argv, **kw):
        super(ZResponse, self).__init__(*argv, **kw)
        self["redirect_url"] = kw.get("redirect_url", url)
        self["url"] = url
        self["request"] = kw.get("request", ZRequest(url, pre_url, -1))
        self["status_code"] = kw.get("status_code", -1)
        self["text"] = kw.get("text", None)
        self["raw_text"] = kw.get("raw_text", None)
        self["headers"] = kw.get("header", {})
        self["crawl_time"] = kw.get("crawl_time", time.time())
        self["error"] = kw.get("error", None)
        self["cost_time"] = kw.get("cost_time", None)
        self["status_code"] = kw.get("status_code", 599)


class Task(Fileds):
    def __init__(self, url, *argv, **kw):
        super(Task, self).__init__(*argv, **kw)
        self["url"] = url
        self["headers"] = kw.get("headers", {})
        self["text"] = kw.get("text", "None")
        self["crawled_time"] = kw.get("crawl_time", time.time())
        self["link_time"] = kw.get("link_time")
        self["cookies"] = kw.get("cookies", {})
