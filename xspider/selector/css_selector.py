#coding=utf-8


from selector import Selector 
from lxml import etree
try:
    from bs4 import BeautifulSoup
except:
    from BeautifulSoup import BeautifulSoup 


class CssSelector(Selector):



    def __init__(self , **kw):
        super(CssSelector , self).__init__("css" ,**kw)
        self.tag = kw.get("tag" , "") 
        self.attr = kw.get("attr" , "")

    def finds(self ,page):
        soup = page.get_soup()
        return [ item.get(self.attr) for item in soup.findAll(self.tag) if item ] 
