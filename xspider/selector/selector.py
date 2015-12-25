# coding=utf-8





class Selector(object):

    
    def __init__(self ,type  ,**kw):
        self.type = type
 
    def finds(self, page):
        raise NotImplementedError

    def __str__(self):
        return "type<{type}> {\"raw_text\":{raw_text}}".format(type = self.type , raw_text = self.raw_text)

