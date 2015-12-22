# coding=utf-8


from ..model.models import ZResponse




class BaseExtractor(object):

    
    def __init__(self , response):
        if isinstance(response , ZResponse):
            self.html = response["text"] 
        elif isinstance(response , basestring):
            self.html = response
 
    def extract(self, response , *argv , **kw):
        raise NotImplementedError
