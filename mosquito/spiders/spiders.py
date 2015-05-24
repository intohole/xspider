# coding=utf-8


class _BaseSpider(object):

    def __init__(self, start_urls):
        self.start_urls = [start_urls] if isinstance(
            start_urls, (str)) else start_urls

    def run(self, *argv, **kw):
        raise NotImplementedError
