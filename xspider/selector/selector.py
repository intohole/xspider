# coding=utf-8


from ..model.models import ZResponse




class Selector(object):

    
    def __init__(self , selector_type, response):
        if isinstance(response , ZResponse):
            self.raw_text = response["text"] 
        elif isinstance(response , basestring):
            self.raw_text = response
        self.type = selector_type 
 
    def extract(self, default = None , *argv , **kw):
        raise NotImplementedError

    def __str__(self):
        return "type<{type}> {\"raw_text\":{raw_text}}".format(type = self.type , raw_text = self.raw_text)

