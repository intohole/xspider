#coding=utf-8






from xspider.filters import urlfilter

url_filter = urlfilter.UrlStartFilter("http://githuber.cn/people/")

print url_filter.filter("http://githuber.cn/people/2503423")
 
