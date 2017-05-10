# coding=utf-8





class Selector(object):

    
    def __init__(self ,type,**kw):
        self.type = type
 
    def finds(self, page):
        raise NotImplementedError
    
    def select(self,page):
        raise NotImplementedError

    def __str__(self):
        return "selector name %s" % self.type
