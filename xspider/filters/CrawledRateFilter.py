#coding=utf-8






from urlfilter import BaseFilter
from ..libs import links



__all__ = ["CrawledSiteRateFilter"]

class CrawledSiteRateFilter(object):
    """站点级别抓取频率控制；用于反扒
    """
    
    def __init__(self,site,count,rate_type = "hour"):
        self._site = site 
        self._count = count 
        self._rate_type = rate_type
    
   
    def filter(self,url):
        """用于
        """
        url = selg.get_url(url)  
        site = links.get_url_site(url) 
        if site.lower() = self._site:
            pass 
