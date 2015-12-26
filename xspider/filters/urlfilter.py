#coding=utf-8

from ..libs import links
import re


class _Filter(object):


    def filter(self , url):
        raise NotImplmentError


class SiteFilter(object):
    """根据站点过滤
        >>> sitefilter = SiteFilter()
    """

    def __init__(self , sites):
        self.sites = set()    
        self._add_site(sites)
    def _add_site(self , site):
        if site:
            if isinstance(site , basestring):
                self.sites.add(site)
            elif isinstance(site , (list , tuple , set)):
                self.sites.update(site)   
            elif:
                raise ValueError


    def filter(self , url):
        url_site = links.get_url_site(url) 
        if url_site in self.sites:
            return False 
        return True 



class UrlRegxFilter(object):
    """链接正则过滤类
        test:
            >>> url_filter = UrlRegxFilter("test.com/xxx[0-9]*")
            >>> url_filter.filter("test.com/xxx3")
            >>> url_filter.filter("test.com/xx4")
    """

    def __init__(self , url_regx):
        if url_regx and isinstance(url_regx , basestring):
            self.url_pattern = re.compile(url_regx)
        else:
            raise ValueError

    def filter(self , url):
        if url and isinstance(url , dict) and "url" in dict:
            url = url["url"]
        elif url and hasattr(url , "url"):
            url = getattr(url , "url")
        elif ( url and isinstance(url , basestring)) is False:
            raise ValueError
        group = self.url_pattern.match(url)
        if group is None:
            return False
        return True
