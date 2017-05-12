#coding=utf-8

from selector import BaseSelector
from b2.json2 import json2
import json

class JsonExtractor(BaseExtractor):

    def __init__(self ,  **kw):
        super(JsonExtractor , self).__init__("json" , **kw)
        self.paths = kw.get("paths" , None)
        if isinstance(self.paths , basestring):
            self.paths = self.paths.split()
        if isinstance(self.paths , (list , tuple)) is False:
            raise ValueError
        self.query = kw.get("query" , None) 
        if self.query is None and self.paths is None:
            raise ValueError
        self.jpath = json2.JPath() 


    def finds(self , page):
        if self.query:
            return self.jpath(page.get_json() , self.query) 

    def find(self , page):
        pass
