#coding=utf-8





from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter
from kuailiyu import KuaiLiYu
from b2 import system2
system2.reload_utf8()
if __name__ == "__main__":
    spider = BaseSpider(name = "kuailiyu"  , page_processor = KuaiLiYu() , allow_site = ["kuailiyu.cyzone.cn"] , start_urls = ["http://kuailiyu.cyzone.cn/"])
    spider.url_filters.append(urlfilter.UrlRegxFilter(["kuailiyu.cyzone.cn/article/[0-9]*\.html$","kuailiyu.cyzone.cn/index_[0-9]+.html$"]))
    spider.start()
