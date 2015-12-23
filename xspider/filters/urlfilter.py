#coding=utf-8

from ..libs import links

class _Filter(object):


    def filter(self , url):
        raise NotImplmentError


class SiteFilter(object):


    def __init__(self , sites):
        self.sites = set()    
        if sites and isinstance(sites ,basestring):
            self.sites.add(sites)
        elif sites and isinstance(sites , (list , tuple, set)):
            self.sites.update(sites)

    
    def filter(self , url):
        url_site = links.get_url_site(url) 
        if url_site in self.sites:
            return True
        return False
