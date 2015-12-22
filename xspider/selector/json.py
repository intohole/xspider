#coding=utf-8


from extractor import BaseExtractor
import json

class JsonExtractor(BaseExtractor):

    def __init__(self , response , *argv , **kw):
        super(JsonExtractor , self).__init__(response)
        self.json = json.loads(self.text) 

    def get(self , *argv , **kw):
        for filed in argv:

