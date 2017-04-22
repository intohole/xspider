#coding=utf-8





from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter
from xspider import processor
from xspider.selector import xpath_selector
from xspider.model.fileds import Fileds

class Kr36(processor.PageProcessor.PageProcessor):


    def __init__(self):
        super(Kr36 , self ).__init__()
        self.title_extractor = xpath_selector.XpathSelector(path = "//title/text()")
    
    def process(self,page,spider):
        item = Fileds()
        title = self.title_extractor.find(page) 
        item["title"] = title
        return item         
if __name__ == "__main__":
    url_filters = [urlfilter.UrlRegxFilter("36kr.com/p/[0-9]+\.html")]    
    spider = BaseSpider(name = "36kr"  , page_processor = Kr36() , allow_site = ["36kr.com"] , start_urls = ["http://www.36kr.com/"])
    spider.start()
