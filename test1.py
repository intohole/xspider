#coding=utf-8





from xspider.spider.spider import BaseSpider
from xspider.filters import urlfilter
from kuailiyu import KuaiLiYu

if __name__ == "__main__":
    spider = BaseSpider(name = "kuailiyu"  , page_processor = KuaiLiYu() , allow_site = ["kuailiyu.cyzone.cn"] , start_urls = ["http://architecturewards.com/"])
    spider.start()
