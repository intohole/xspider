#coding=utf-8





from xspider.spider.spider import BaseSpider

if __name__ == "__main__":
    spider = BaseSpider(name = "test" ,start_urls = ["http://www.126.com"])
    spider.start()
