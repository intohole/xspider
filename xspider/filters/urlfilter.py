#coding=utf-8

from ..libs import links
import re


class _Filter(object):

    def __init__(self , filter_name):
        self.filter_name = filter_name

    def filter(self , url):
        raise NotImplmentError


class SiteFilter(_Filter):
    """根据站点过滤
        >>> sitefilter = SiteFilter()
    """

    def __init__(self , sites):
        super(SiteFilter , self).__init__("site_filter")
        self.sites = set()    
        self._add_site(sites)

    def _add_site(self , site):
        if site:
            if isinstance(site , basestring):
                self.sites.add(site)
            elif isinstance(site , (list , tuple , set)):
                self.sites.update(site)   
            else:
                raise ValueError


    def filter(self , url):
        url_site = links.get_url_site(url) 
        if url_site in self.sites:
            return False 
        return True 



class UrlRegxFilter(_Filter):
    """链接正则过滤类
        test:
            >>> url_filter = UrlRegxFilter("test.com/xxx[0-9]*")
            >>> url_filter.filter("test.com/xxx3")
            >>> url_filter.filter("test.com/xx4")
    """

    def __init__(self , url_regxs):
        super(UrlRegxFilter , self).__init__("url_regx")
        if url_regxs and isinstance(url_regxs, basestring):
            self.url_patterns = [re.compile(url_regxs)]
        elif url_regxs and isinstance(url_regxs , (list , tuple)):
            self.url_patterns = [re.compile(url_regx) for url_regx in url_regxs]
        else:
            raise ValueError

    def filter(self , url):
        if url and isinstance(url , dict) and "url" in dict:
            url = url["url"]
        elif url and hasattr(url , "url"):
            url = getattr(url , "url")
        elif ( url and isinstance(url , basestring)) is False:
            raise ValueError
        for pattern in self.url_patterns:
            group = pattern.search(url)
            if group:
                return False        
        return True 
