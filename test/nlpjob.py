
from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter


class Nlpjob(processor.PageProcessor.PageProcessor):


    def __init__(self):
        pass

    def process(slef , page , spider):
        pass

if __name__ == "__main__":
    spider = BaseSpider(name = "nlpjob"  , page_processor = KuaiLiYu() , allow_site = ["kuailiyu.cyzone.cn"] , start_urls = ["http://kuailiyu.cyzone.cn/"])
    spider.url_filters.append(urlfilter.UrlRegxFilter(["kuailiyu.cyzone.cn/article/[0-9]*\.html$","kuailiyu.cyzone.cn/index_[0-9]+.html$"]))
    spider.start()
