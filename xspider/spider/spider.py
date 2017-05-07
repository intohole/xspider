#coding=utf-8



from b2 import log2
from b2 import rand2
from ..fetch.fetcher import BaseRequestsFetcher
from ..model.models import ZRequest
from ..model.page import Page
from ..processor.PageProcessor import SimplePageProcessor
from ..pipeline.ConsolePipeLine import ConsolePipeLine
from ..queue.base_queue import DumpSetQueue
from ..libs import links
from ..model.page import Page
from ..filters.urlfilter import SiteFilter
from spider_listener import SpiderListener
from ..selector.css_selector import CssSelector
from spider_listener import DefaultSpiderListener

class BaseSpider(object):


    def __init__(self , name, *argv , **kw):
        self.name = name
        self.allow_site = kw.get("allow_site" , [])
        self.start_urls = kw.get("start_urls" , [])
        self.page_processor = kw.get("page_processor" , SimplePageProcessor())
        self.fetcher = kw.get("fetcher" , BaseRequestsFetcher())
        self.pipelines = kw.get("pipeline" , [ConsolePipeLine()])
        self.run_flag = True
        self.spid = rand2.get_random_seq(10)
        self.url_pool = kw.get("queue" , DumpSetQueue(10000))
        self.log_level = kw.get("log_level" , "warn")
        self.logger = log2.get_stream_logger(self.log_level)
        self.logger.info("init")
        self.site_filters = [SiteFilter(site) for site in self.allow_site]
        self.url_filters = kw.get("url_filters",[])
        self.listeners = SpiderListener()
        self.listeners.addListener(kw.get("listeners" , [DefaultSpiderListener()]))
        self.link_extractors = CssSelector(tag = "a" , attr = "href")

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
                _links = self.extract_links(page)
                links.update(self.url_filter(_links))
                items = self.page_processor.process(page , self)
                if items is None:
                    continue
                self.pipeline(items)
            for link in links:
                self.url_pool.put_request(ZRequest(link , request["dir_path"] , *argv , **kw))
        self.crawl_stop()


    def _make_start_request(self , *argv , **kw):
        for url in self.start_urls:
            self.logger.debug("add start url [{url}]".format(url = url))
            self.url_pool.put_request(ZRequest(url , 0 ,*argv , **kw ))

    def extract_links(self , page):
        parrent_link = page.request["url"]
        parrent_site = links.get_url_site(parrent_link)
        parrent_protocol = links.get_url_protocol(parrent_link)
        return [ links.join_url(parrent_protocol,parrent_site , url ) for url in self.link_extractors.finds(page) if url  ]

    def pipeline(self , page ):
        for pipeline in self.pipelines:
            pipeline.process(page)

    def url_filter(self , urls):
        if len(self.url_filters) == 0:
            return urls
        site_url = []
        if len(self.site_filters):
            for url in urls:
                for site_filter in  self.site_filters:
                    if not site_filter.filter(url):
                        site_url.append(url) 
                        break
        else:
            site_url.extend(urls) 
        urls_result = []
        for url in site_url:
            for urlfilter in self.url_filters:
                if not urlfilter.filter(url): #链接没有通过过滤器，返回True
                    urls_result.append(url)
                    break
        return  urls_result 

    def crawl_stop(self):
        self.listeners.notify("spider_stop" ,self)

    def crawl_start(self):
        self.listener.notity("spider_start" ,self)
