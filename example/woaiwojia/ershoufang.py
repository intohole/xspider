#coding=utf-8

from xspider.spider.spider import BaseSpider
from xspider.filters import UrlFilter
from xspider.processor import PageProcessor
from xspider.selector import XPathSelector
from xspider.filters.CrawledFilter import SimpleCrawledFilter
from xspider.filters import CrawlRateFilter
from xspider.pipeline import FilePipeLine
from xspider import model
from xspider.fetch import tornado_fetcher
from b2 import system2
system2.reload_utf8()
from lxml import etree


class WoAiWoJia2Fang(PageProcessor.PageProcessor):
    def __init__(self):
        super(WoAiWoJia2Fang, self).__init__()
        self.fang_info = XPathSelector.XpathSelector(
            path="//ul[@class='pList']/li/div[@class='listCon']")

    def process(self, page, spider):
        items = model.fileds.Fileds()
        for node in self.fang_info.finds(page):
            node = etree.HTML(etree.tostring(node))
            fang_id = node.xpath("//h3[@class='listTit']/a/@href")[0].split(
                "/")[-1].split(".")[0]
            items[fang_id] = model.fileds.Fileds()
            items[fang_id]["title"] = node.xpath(
                "//h3[@class='listTit']/a/text()")
            items[fang_id]["intro"] = node.xpath(
                "//div[@class='listX']/p[1]/text()")
            items[fang_id]["location"] = node.xpath(
                "//div[@class='listX']/p[2]/text()")
            items[fang_id]["daikan"] = node.xpath(
                "//div[@class='listX']/p[3]/text()")
            items[fang_id]["sumPrice"] = node.xpath(
                "//div[@class='listX']/div[@class='jia']/p[1]/text()")
            items[fang_id]["price"] = node.xpath(
                "//div[@class='listX']/div[@class='jia']/p[2]/text()")
            items[fang_id]["tag"] = node.xpath(
                "//div[@class='listTag']/text()")
        items["url"] = page.url
        return items


if __name__ == "__main__":
    start_url_filter = UrlFilter.UrlStartFilter(
        "https://hz.5i5j.com/ershoufang/n")
    start_url_filter.set_must_check()

    url_filters = [
        CrawlRateFilter.TimeRateFilter(every=0.5, wait=2), start_url_filter
    ]
    spider = BaseSpider(
        name="woaiwojia.hz",
        #fetcher=tornado_fetcher.Fetcher(),
        url_filters=url_filters,
        crawled_filter=SimpleCrawledFilter(),
        page_processor=WoAiWoJia2Fang(),
        pipeline=[FilePipeLine.DumpFilePipe()],
        timeout=400,
        allow_site=["hz.5i5j.com"],
        start_urls=["https://hz.5i5j.com/ershoufang/"])
    spider.start()
