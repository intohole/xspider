#coding=utf-8



from b2 import log2
from b2 import rand2
from ..fetch.fetcher import BaseFetcher 
from ..model.models import ZReques
import random

class _BaseSpider(object):

    def __init__(self, start_urls):
        self.start_urls = [start_urls] if isinstance(
            start_urls, (basestring)) else start_urls

    def run(self, *argv, **kw):
        raise NotImplementedError


class BaseSpider(_BaseSpider):


    def __init__(self , start_urls , page_processor = None , log_level = 'DEBUG' , fetch_type = None , *argv , **kw):
        self.start_urls = start_urls
        self.crawled = set()
        self.name = name  
        self.logger = log2.get_stream_logger(log_level)
        self.page_processor = page_processor 
        self.fetcher = BaseFetcher()
        self.run_flag = True
        self.spid = rand2.get_random_seq(10) 
    
    def _check_spider(self):
        pass

    def run(self, *argv , **kw):
        self.crawl_start( self.start_urls  , self.url_pool , self.page_processor)
        while len(self.url_pool) > 0 self.run_flag:
            request = self.url_pool.get()
            for page in self.fetcher.fetch(request):
                item = self.pieline(self.page_processor.extract(page))
                self.pieline.excute(item)
        self.crawl_stop()
            
            
    def on_setup(self):
        for url in start_urls:
            self.url_pool.add(ZReques)

    def crawl_stop(self):
        self.pieline.destory(self)
