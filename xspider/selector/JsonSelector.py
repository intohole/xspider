#coding=utf-8

from selector import BaseSelector
from b2.json2 import json2
import json
from b2 import exceptions2

class JsonSelector(BaseSelector):

    def __init__(self ,  **kw):
        super(JsonSelector , self).__init__("json" , **kw)
        self.query = kw.get("query" , None) 
        exceptions2.judge_null(self.query)
        self.jpath = json2.JPath(self.query) 


    def finds(self , page):
        if self.query:
            return self.jpath(page.get_json() , self.query) 

    def find(self , page):
        pass
