#coding=utf-8



from b2 import log2
from b2 import rand2
from ..fetch.fetcher import BaseRequestsFetcher
from ..model.models import ZRequest
from ..model.page import Page
from ..processor.PageProcessor import SimplePageProcessor
from ..pieline.ConsolePipeLine import ConsolePipeLine
from ..queue.base_queue import DumpSetQueue
from ..libs import links
from ..model.page import Page
from ..filters.urlfilter import SiteFilter
from spider_listener import SpiderListener
from ..selector.css_selector import CssSelector
from spider_listener import DefaultSpiderListener

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
        self.pielines = kw.get("pieline" , [ConsolePipeLine()])
        self.run_flag = True
        self.spid = rand2.get_random_seq(10)
        self.url_pool = kw.get("queue" , DumpSetQueue(10000))
        self.log_level = kw.get("log_level" , "DEBUG")
        self.logger = log2.get_stream_logger(self.log_level)
        self.logger.info("init")
        self.url_filters = kw.get("url_filters" ,[SiteFilter(self.allow_site)] )
        self.listeners = SpiderListener()
        self.listeners.addListener(kw.get("listeners" , [DefaultSpiderListener()]))
        self.link_extractors = CssSelector(tag = "a" , attr = "href")

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
                page = Page(request , response , request["dir_path"])
                items = self.page_processor.process(page , self)
                self.pieline(items)
                _links = self.extract_links(page)
                links.update(self.url_filter(_links))
            for link in links:
                self.url_pool.put_request(ZRequest(link , request["dir_path"] , *argv , **kw))
        self.crawl_stop()


    def _make_start_request(self , *argv , **kw):
        for url in self.start_urls:
            self.logger.debug("add start url [{url}]".format(url = url))
            self.url_pool.put_request(ZRequest(url , 0 ,*argv , **kw ))

    def extract_links(self , page):
        pre_link = page.request["url"]
        site = links.get_url_site(pre_link)
        return [ links.join_url(site , url ) for url in self.link_extractors.finds(page) ]

    def pieline(self , page ):
        for pieline in self.pielines:
            pieline.process(page)

    def url_filter(self , urls):
        if len(self.url_filters) == 0:
            return urls
        _urls = []
        for url in urls:
            is_skip = False
            for urlfilter in self.url_filters:
                if urlfilter.filter(url) is True: #链接没有通过过滤器，返回True
                    is_skip = True
                    break
            if is_skip is False: #链接通过所有过滤
                _urls.append( url)
            else:
                self.logger.info("url:%s is skip !" % url)
        return  _urls

    def crawl_stop(self):
        self.listeners.notify("spider_stop" ,self)

    def crawl_start(self):
        self.listener.notity("spider_start" ,self)
