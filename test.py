#coding=utf-8





from xspider.spider.spider import BaseSpider

if __name__ == "__main__":
    spider = BaseSpider(name = "36kr" ,allow_site = ["www.36kr.com"],start_urls = ["http://www.36kr.com"])
    spider.start()
