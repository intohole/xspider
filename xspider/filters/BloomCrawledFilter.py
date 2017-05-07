#coding=utf-8




import pybloomfilter
from urlfilter import BaseFilter
import os



__all__ = ["BloomCrawledFilter"]


class BloomCrawledFilter(BaseFilter):
    


    def __init__(self,bloom_file,url_size,error_rate = 0.001):
        """初始化bloom抓取链接功能
            param:bloom_file:basestring:bloom过滤器存储文件，用于持久化
            param:url_size:int:初始化链接库抓取的大小
            param:error_rate:float:bloom允许出错概率
            return:None:None
            Test:
                >>> bloom = BloomCrawledFilter(".tmp",1000)
                >>> bloom.filter("https://www.baidu.com")
                >>> bloom.filter("https://www.baidu.com")
                >>> bloom1 = BloomCrawledFilter(".tmp",1000)
                >>> bloom.filter("https://www.baidu.com")
                >>> bloom.filter("https://www.baidu.com")
        """
        self.bloom = None
        self.bloom_file = bloom_file
        self.error_rate = error_rate
        self.url_size = url_size
        if os.path.exists(self.bloom_file):
            self.bloom = pybloomfilter.BloomFilter.open(self.bloom_file) 
        else:
            self.bloom = pybloomfilter.BloomFilter(self.url_size,self.error_rate,self.bloom_file)
 
    def filter(self,url):
        url = self.get_url(url)      
        if url in self.bloom:
            return True
        self.bloom.add(url)
        return False

