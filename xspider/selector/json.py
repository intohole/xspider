#coding=utf-8


from extractor import BaseExtractor
from b2.type2 import 
import json

class JsonExtractor(BaseExtractor):

    def __init__(self ,  **kw):
        super(JsonExtractor , self).__init__("json" , **kw)
        self.paths = kw.get("paths" , [])
        if isinstance(self.paths , basestring):
            self.paths = self.paths.split()
        if isinstance(self.paths , (list , tuple)) is False:
            raise ValueError
    


    def finds(self , page):
        json = page.get_json()
        for p in paths:
            pass  

    def find(self , page):
        pass
