#coding=utf-8



from b2 import log2
from b2 import rand2
from ..fetch.fetcher import BaseRequestsFetcher 
from ..model.models import ZRequest
from ..model.page import Page
from ..processor.PageProcessor import SimplePageProcessor
from ..pieline.ConslePieLine import ConslePieLine
from ..queue.base_queue import DumpSetQueue 

class _BaseSpider(object):

    def __init__(self, start_urls):
        self.start_urls = [start_urls] if isinstance(
            start_urls, (basestring)) else start_urls

    def run(self, *argv, **kw):
        raise NotImplementedError


class BaseSpider(_BaseSpider):


    def __init__(self , name, start_urls = None ,pieline = None ,  page_processor = None , log_level = 'DEBUG' , fetch_type = None , *argv , **kw):
        self.logger = log2.get_stream_logger(log_level)
        self.start_urls = [] if start_urls is None  else start_urls 
        self.name = name  
        self.logger.info("init start urls {urls}".format(urls = start_urls))
        self.page_processor = page_processor if page_processor else SimplePageProcessor() 
        self.fetcher = fetch_type if fetch_type else BaseRequestsFetcher()
        self.pieline = pieline if pieline else ConslePieLine()
        self.run_flag = True
        self.spid = rand2.get_random_seq(10) 
        self.url_pool = DumpSetQueue() 
        self.logger.info("init")
    
    def _check_spider(self):
        pass
    
    def setStartUrls(self , urls):
        self.start_urls.extend(urls)

    def start(self, *argv , **kw):
        self._make_start_request(*argv , **kw)
        self.logger.info("spider {name} start run ".format(name = self.name))
        while self.url_pool.empty() is False and self.run_flag:
            request = self.url_pool.get_request()
            print request
            self.logger.info("get {req} ".format(req = request))
            for page in self.fetcher.fetch(request):
                self.pieline.process(self.page_processor.extract(page))
        self.crawl_stop()
            
            
    def _make_start_request(self , *argv , **kw):
        for url in self.start_urls:
            self.logger.debug("add start url [{url}]".format(url = url))
            self.url_pool.put_request(ZRequest(url ,*argv , **kw ))

    def crawl_stop(self):
        self.pieline.destory(self)
