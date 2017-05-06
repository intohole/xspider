#coding=utf-8





from xspider.filters import  crawledFilter



url_filter = crawledFilter.SimpleCrawledFilter()
print url_filter.filter("https://www.baidu.com")
print url_filter.filter("https://www.baidu.com")
