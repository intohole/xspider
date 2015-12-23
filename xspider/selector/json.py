#coding=utf-8


from extractor import BaseExtractor
from b2.type2 import 
import json

class JsonExtractor(BaseExtractor):

    def __init__(self , response , *argv , **kw):
        super(JsonExtractor , self).__init__(response)
        self.json = json.loads(self.raw_text) 
