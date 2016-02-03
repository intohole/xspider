#coding=utf-8





from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter
from xspider import processor 
from xspider.selector import xpath_selector
from xspider import model
from xspider import urlfilter

class 36Kr(processor.PageProcessor.PageProcessor):


    def __init__(self):
        super(36Kr , self ).__init__()
        self.title_extractor = xpath_selector.XpathSelector(path = "//title/text()")
    

    def process(self , page , spider):
        items 
if __name__ == "__main__":
    spider = BaseSpider(name = "kuailiyu"  , page_processor = KuaiLiYu() , allow_site = ["architecturewards.com"] , start_urls = ["http://architecturewards.com/"])
    spider.start()
