#coding=utf-8





from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter

if __name__ == "__main__":
    spider = BaseSpider(name = "kuailiyu" , allow_site = ["kuailiyu.cyzone.cn"] , start_urls = ["http://kuailiyu.cyzone.cn/"])
    spider.url_filters.append(urlfilter.UrlRegxFilter("kuailiyu.cyzone.cn/article/[0-9]*\.html$"))
    spider.start()
