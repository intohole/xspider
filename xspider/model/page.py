#coding=utf-8

from ..selector.css_selector import CssSelector 
import json 
from lxml import etree
try:
    from bs4 import BeautifulSoup
    # 应该将方法都归一化成一个 ， 后续会阅读文档做下
except:
    from BeautifulSoup import BeautifulSoup 



class Page(object):



    def __init__(self ,request , response ):
        self.request = request
        self.json = None 
        self.raw_text = response["text"]
        self.soup = None 
        self.container = {}
        self.etree = None
    

    def get_soup(self):
        if self.soup is None:
            self.soup = BeautifulSoup(self.raw_text)
        return self.soup
    
    def get_json(self):
        if self.json is None:
            self.json = json.loads(self.raw_text)
        return self.json 

    def get_tree(self):
        if self.etree is None:
            self.etree = etree(self.raw_text) 
        return self.etree
