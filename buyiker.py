#coding=utf-8



from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter
from xspider import processor 
from xspider.selector import xpath_selector
from xspider import model


class BuYiKr(processor.PageProcessor.PageProcessor):


    def __init__(self):
        super(BuYiKr , self).__init__()
        self.title_extractor = xpath_selector.XpathSelector(path = "//title/text()")

    def process(self , page , spider):
        items = model.fileds.Fileds()
        items["title"] = self.title_extractor.find(page)
        items["url"] = page.url
        return items

if __name__ == "__main__":
    spider = BaseSpider(name = "buyikr"  , page_processor = BuYiKr() , allow_site = ["buyiker.com"] , start_urls = ["http://buyiker.com/"])
    #spider.url_filters.append(urlfilter.UrlRegxFilter(["kuailiyu.cyzone.cn/article/[0-9]*\.html$","kuailiyu.cyzone.cn/index_[0-9]+.html$"]))
    spider.start()
