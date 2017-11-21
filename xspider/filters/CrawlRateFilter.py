#coding=utf-8






from UrlFilter import BaseFilter
from ..libs import links
import time


__all__ = ["CrawledSiteRateFilter"]
class SiteRateInfo(object):
    
    def __init__(self,site,time_type,max_count):
        self.site = site 
        self.count = 0
        self.time_type = time_type
        self.max_count = 0
        self.time = time.time() 

    def dec(self):
        pass    

    def isChange(self):
        pass 

class CrawledSiteRateFilter(object):
    """站点级别抓取频率控制；用于反扒
    """
    
    def __init__(self,site,count,rate_type = "hour"):
        pass
   
    def filter(self,url):
        """用于
        """
        url = selg.get_url(url)  
        site = links.get_url_site(url) 
        if site.lower() == self._site:
            pass 
     
