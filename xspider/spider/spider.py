#coding=utf-8



from b2 import log2
from b2 import rand2
from ..fetch.fetcher import BaseRequestsFetcher 
from ..model.models import ZRequest
from ..model.page import Page
from ..processor.PageProcessor import SimplePageProcessor
from ..pieline.ConslePieLine import ConslePieLine
from ..queue.base_queue import DumpSetQueue 
from ..libs import links
from ..model.page import Page
from ..filters.urlfilter import SiteFilter

class _BaseSpider(object):

    def __init__(self, start_urls):
        self.start_urls = [start_urls] if isinstance(
            start_urls, (basestring)) else start_urls

    def run(self, *argv, **kw):
        raise NotImplementedError


class BaseSpider(_BaseSpider):


    def __init__(self , name, *argv , **kw):
        self.name = name  
        self.allow_site = kw.get("allow_site" , []) 
        self.start_urls = kw.get("start_urls" , []) 
        self.page_processor = kw.get("page_processor" , SimplePageProcessor()) 
        self.fetcher = kw.get("fetcher" , BaseRequestsFetcher()) 
        self.pielines = kw.get("pieline" , [ConslePieLine()]) 
        self.run_flag = True
        self.spid = rand2.get_random_seq(10) 
        self.url_pool = kw.get("queue" , DumpSetQueue(10000)) 
        self.log_level = kw.get("log_level" , "DEBUG")
        self.logger = log2.get_stream_logger(self.log_level)
        self.logger.info("init")
        self.url_filters = kw.get("url_filters" ,[SiteFilter(self.allow_site)] ) 
    
    def _check_spider(self):
        pass

    
    def setStartUrls(self , urls):
        self.start_urls.extend(urls)

    def start(self, *argv , **kw):
        self._make_start_request(*argv , **kw)
        while self.url_pool.empty() is False and self.run_flag:
            request = self.url_pool.get_request()
            self.logger.info("get {req} ".format(req = request))
            links = set() 
            for response in self.fetcher.fetch(request):
                page = Page(request , response) 
                items = self.page_processor.extract(page)
                self.process(items)
                _links = self.extract_links(page)
                links.update(self.url_filter(_links))
            for link in links:
                self.url_pool.put_request(ZRequest(link , *argv , **kw))
        self.crawl_stop()
            
            
    def _make_start_request(self , *argv , **kw):
        for url in self.start_urls:
            self.logger.debug("add start url [{url}]".format(url = url))
            self.url_pool.put_request(ZRequest(url ,*argv , **kw ))
    
    def extract_links(self , page):
        pre_link = page.request["url"]
        site = links.get_url_site(pre_link)
        return [ links.join_url(site , link.get("href")) for link in page.css().findAll("a")  if link is not None ]

    def process(self , page ):
        for pieline in self.pielines:
            pieline.process(page)

    def url_filter(self , urls):
        _urls = []
        for url in urls:
            is_cool = True 
            for urlfilter in self.url_filters:
                if urlfilter.filter(url):
                    is_cool = False
                    break
            if is_cool:
                _urls.append( url)
        return  _urls                 

    def crawl_stop(self):
        for pieline in self.pielines:
            pieline.destory(self)
