#coding=utf-8

from b2 import exceptions2 
from ..model.fileds import Fileds

class PageProcessor(object):
    """parse page or extract web fileds or do somthing 
    """

    def process(self , page , spider):
        raise NotImplmentError

    def match(self,page):
        return True





class PageMatchStartUrlProcessor(object):
    
    
    def __init__(self,start_url_pattern,lower = True):    
        super(PageProcessor,self).__init__()
        if start_url_pattern is None:
            raise ValueError("start_url_pattern must be bastring and have value")
        if not isinstance(start_url_pattern,basestring):
            exceptions2.raiseTypeError(start_url_pattern)
        self.start_url_pattern = start_url_pattern if lower is False else start_url_pattern.lower()
        self.lower = lower 
         
    def match(self,page):
        url = page["url"].lower() if self.lower else page["url"] 
        if url.startswith(self.start_url_pattern):
            return True
        return False
