#coding=utf-8

from b2 import log2
from b2 import rand2
from b2 import str2
from b2 import sort2
from ..fetch.fetcher import BaseRequestsFetcher
from ..model.models import ZRequest
from ..model.page import Page
from ..pipeline.ConsolePipeLine import ConsolePipeLine
from ..queue.SpiderQueue import MemoryFifoQueue
from ..libs import links
from ..model.page import Page
from ..filters.UrlFilter import SiteFilter
from ..selector.CssSelector import CssSelector
from spiderlistener import DefaultSpiderListener
from spiderlistener import SpiderListener
from b2 import exceptions2
import json
from ..processor.PageProcessor import PageProcessor


class BaseSpider(object):
    def __init__(self, name, *argv, **kw):
        self.log_level = kw.get("log_level", "warn")
        self.logger = log2.get_stream_logger(self.log_level, name)
        self.name = name
        self.allow_site = kw.get("allow_site", [])
        self.logger.info("spider {} init , allow_site {}".format(
            name, self.allow_site))
        self.start_urls = kw.get("start_urls", [])
        exceptions2.judge_null(self.start_urls)
        self.page_processor = kw.get("page_processor")
        exceptions2.judge_null(self.page_processor)
        exceptions2.judge_type(self.page_processor, PageProcessor)
        self.fetcher = kw.get("fetcher", BaseRequestsFetcher())
        self.pipelines = kw.get("pipeline", [ConsolePipeLine()])
        self.run_flag = True
        self.spid = rand2.get_random_seq(10)
        self.url_pool = kw.get("queue", MemoryFifoQueue(10000))
        self.logger.info("init")
        self.before_crawl = kw.get("before_crawl",
                                   [])  # before crawl do something
        self.site_filters = [SiteFilter(site) for site in self.allow_site]
        url_filters = kw.get("url_filters", [])
        url_filters.extend(self.site_filters)
        sort2.sort_list_object(url_filters, "_priority")
        self.url_filters = url_filters
        self.listeners = SpiderListener()
        self.fetch_coding = kw.get("fetch_coding", None)
        self.listeners.addListener(
            kw.get("listeners", [DefaultSpiderListener()]))
        self.link_extractors = CssSelector("a[href]")
        self.crawled_filter = kw.get("crawled_filter", None)

    def setStartUrls(self, urls):
        self.start_urls.extend(urls)

    def start(self, *argv, **kw):
        self.crawl_start()
        kw["fetch_coding"] = self.fetch_coding
        self._make_start_request(*argv, **kw)
        self.logger.info("spider {} get start request".format(self.name))
        while self.url_pool.empty() is False and self.run_flag:
            request = self.url_pool.pop()
            self.logger.info("get {req} ".format(req=request))
            links = set()
            for response in self.fetcher.fetch(request):
                page = Page(request, response, request["dir_path"])
                requests = [
                    self._make_request(link, request)
                    for link in self.extract_links(page) if link not in links
                ]
                links.update(request["url"] for request in requests)
                requests = self.url_filter(requests)
                self.logger.debug("extract link {}".format(links))
                items = self.page_processor.excute(page, self)
                self.logger.debug("process items {} items {}".format(
                    request["url"], json.dumps(items)))
                if items:
                    self.pipeline(items)
                for request in requests:
                    self.url_pool.push(request)
        self.crawl_stop()

    def _make_request(self, link, request, *argv, **kw):
        return ZRequest(link, request["pre_url"], request["dir_path"], *argv,
                        **kw)

    def _make_start_request(self, *argv, **kw):
        for url in self.start_urls:
            self.logger.debug("add start url [{url}]".format(url=url))
            self.url_pool.push(ZRequest(url, None, 0, *argv, **kw))

    def extract_links(self, page):
        parrent_link = page.request["url"]
        parrent_site = links.get_url_site(parrent_link)
        parrent_protocol = links.get_url_protocol(parrent_link)
        self.logger.debug(
            "parrent_link {} parrent_site {} parrent_protocol {} ".format(
                parrent_link, parrent_site, parrent_protocol))
        return [
            links.join_url(parrent_protocol, parrent_site, url["href"])
            for url in self.link_extractors.find(page)
            if not str2.isBlank(url["href"])
        ]

    def pipeline(self, page):
        for pipeline in self.pipelines:
            pipeline.process(page)

    def _filter(self, url_filters, url):
        """如果被过滤，则返回True,否则返回False
        """
        for url_filter in url_filters:
            _filter = url_filter.filter(url)
            # if url_filter must be check and url not match filter , so url filtered
            if _filter is True and url_filter.must_check():
                return True
            if not _filter:
                return False
        return True

    def url_filter(self, urls):
        if urls is None or len(urls) == 0:
            return []
        if len(self.url_filters):
            urls[:] = [
                url for url in urls if not self._filter(self.url_filters, url)
            ]
        if self.crawled_filter:
            urls[:] = [
                url for url in urls if not self.crawled_filter.filter(url)
            ]
        return urls

    def crawl_stop(self):
        self.listeners.notify("spider_stop", self)

    def crawl_start(self):
        self.listeners.notify("spider_start", self)
