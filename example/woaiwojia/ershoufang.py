#coding=utf-8

from xspider.spider.spider import BaseSpider
from xspider.filters import UrlFilter
from xspider.processor import PageProcessor
from xspider.selector import XPathSelector
from xspider.filters.CrawledFilter import SimpleCrawledFilter
from xspider.pipeline import FilePipeLine
from xspider import model
from b2 import system2
system2.reload_utf8()
from lxml import etree


class KaiJiang(PageProcessor.PageProcessor):
    def __init__(self):
        super(KaiJiang, self).__init__()
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
        "http://hz.5i5j.com/ershoufang/n")
    start_url_filter.set_must_check()
    url_filters = [start_url_filter]
    spider = BaseSpider(
        name="woaiwojia.hz",
        url_filters=url_filters,
        crawled_filter=SimpleCrawledFilter(),
        page_processor=KaiJiang(),
        pipeline=[FilePipeLine.DumpFilePipe()],
        allow_site=["kaijiang.5.com"],
        start_urls=["http://hz.5i5j.com/ershoufang/n1/"])
    spider.start()
