# coding=utf-8
from b2 import log2
from ..fetch.fetcher import BaseFetcher 

class _BaseSpider(object):

    def __init__(self, start_urls):
        self.start_urls = [start_urls] if isinstance(
            start_urls, (str)) else start_urls

    def run(self, *argv, **kw):
        raise NotImplementedError


class BaseSpider(_BaseSpider):


    def __init__(self , start_urls , page_processor = None , log_level = 'DEBUG'):
        self.start_urls = start_urls
        self.crawled = set()
        self.name = name  
        self.logger = log2.get_stream_logger(log_level)
        self.page_processor = page_processor 
        self.fetcher = BaseFetcher()

    def run(self, *argv , **kw):
        self.crawl_start( self.start_urls  , self.url_pool , self.page_processor)
        while len(self.url_pool) > 0:
            request = self.url_pool.get()
            for page in self.fetcher.fetch(request):
                self.pieline(self.page_processor.extract(page))
        self.crawl_stop()
            
            
    def crawl_start(self):
        pass


    def crawl_stop(self):
        pass
