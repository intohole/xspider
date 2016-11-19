#coding=utf-8





from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter
from xspider import processor
from xspider.selector import xpath_selector
from xspider import model
from xspider import urlfilter

class Kr36(processor.PageProcessor.PageProcessor):


    def __init__(self):
        super(Kr36 , self ).__init__()
        self.title_extractor = xpath_selector.XpathSelector(path = "//title/text()")

if __name__ == "__main__":
    spider = BaseSpider(name = "36kr"  , page_processor = Kr36() , allow_site = ["architecturewards.com"] , start_urls = ["http://architecturewards.com/"])
    spider.start()
