#coding=utf-8





from urlfilter import BaseFilter



__all__ = ["SimpleCrawledFilter"]


class SimpleCrawledFilter(BaseFilter):
    """已抓链接实现
        Test:
            >>> url_filter = SimpleCrawledFilter()
            >>> url_filter.filter("https://www.baidu.com")
            >>> url_filter.filter("https://www.baidu.com")
    """


    def __init__(self):
        super(SimpleCrawledFilter,self).__init__("simple_crawled_filter")
        self.crawled = set()
    


    def filter(self,url):
        url = self.get_url(url)
        if url in self.crawled:
            return True
        self.crawled.add(url)
        return False
