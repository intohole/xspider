#coding=utf-8

from b2 import exceptions2 
from ..model.fileds import Fileds

__all__ = ["PageProcessor","PageMatchStartUrlProcessor"]

class PageProcessor(object):
    """parse page or extract web fileds or do somthing 
    """
    def __init__(self,name = None):
        self.name = name if name else type(self).__name__ 

    def process(self , page , spider):
        raise NotImplmentError

    def match(self,page):
        return True

    def excute(self,page,spider):
        if self.match(page):
            self.process(page,spider)



class PageMatchStartUrlProcessor(PageProcessor):
    """extract web filed by url prefix match
    """    
    
    def __init__(self,name,start_url_pattern,lower = True):    
        """init function
            param:name:bastring:processor name
            param:start_url_pattern:basestring:url prefix  
            param:lower:blooean:lower url match
            exception:ValueError:start_url_pattern is empty 
            exception:TypeError:start_url_pattern's type not basestring
            return:None
        """
        super(PageMatchStartUrlProcessor,self).__init__(name)
        if start_url_pattern is None and len(start_url_pattern) == 0:
            raise ValueError("start_url_pattern must be bastring and have value")
        if not isinstance(start_url_pattern,basestring):
            exceptions2.raiseTypeError(start_url_pattern)
        self.start_url_pattern = start_url_pattern if lower is False else start_url_pattern.lower()
        self.lower = lower 
         
    def match(self,page):
        url = page.request["url"].lower() if self.lower else page["url"] 
        if url.startswith(self.start_url_pattern):
            return True
        return False
