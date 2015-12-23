#coding=utf-8


from extractor import BaseExtractor 

try:
    from bs4 import BeautifulSoup
except:
    from BeautifulSoup import BeautifulSoup 


class CssSelector(BaseExtractor):



    def __init__(self , response):
        super(CssSelector , self).__init__("css" ,response)
        self.soup = BeautifulSoup(self.raw_text)


    def extractor(*argv , **kw):
        pass
