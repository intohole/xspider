#coding=utf-8

import requests
from b2.log2 import get_stream_logger
from xspider.model.models import ZResponse
from xspider.handler.SpiderHandler import LogHandler
import time


class _BaseFetcher(object):
    """基本抓取器
    get_result      得到链接网页信息
    """

    def __init__(self, log_level="DEBUG", handler=LogHandler()):
        self.logger = get_stream_logger(log_level, log_name="fetcher")
        self.handler = handler
        self.proxy_policy = None

    def fetch(self, urls, method='get', *argv, **kw):
        raise NotImplementedError

    def setProxy(self, proxy_policy):
        self.proxy_policy = proxy_policy


class BaseRequestsFetcher(_BaseFetcher):
    """基础抓取器
        通过requests库实现功能，单线程下载链接，适合小爬虫使用
    """

    def __init__(self):
        super(BaseRequestsFetcher, self).__init__()

    def fetch(self, request, method='get', *argv, **kw):
        if request is None:
            self.logger.error("download [%s] is fail" % request)
            yield

        crawl_time = time.time()
        method = getattr(requests, request.method)
        config = {}
        if self.proxy_policy is not None:
            config["proxies"] = self.proxy_policy.getProxy(self, request)
        response = method(
            request.url,
            params=request.params,
            headers=request.headers,
            **config)

        if response and response.status_code == requests.codes.ok:
            yield ZResponse(
                response.url,
                request.pre_url,
                status_code=response.status_code,
                crawl_time=crawl_time,
                raw_text=response.text)
        else:
            self.logger.error(
                "download {url} fail , preurl : {preurl} , status_code: {status_code}".
                format(
                    url=request.url,
                    preurl=request.pre_url,
                    status_code=response.status_code))
