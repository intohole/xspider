#coding=utf-8

import json 
from lxml import etree
from ..libs import links
try:
    from bs4 import BeautifulSoup
    # 应该将方法都归一化成一个 ， 后续会阅读文档做下
except:
    from BeautifulSoup import BeautifulSoup 



class Page(object):
    """页面信息保存体
    """


    def __init__(self ,request , response , dir_path ):
        self.url = request["url"] # 抓取链接 
        self.site = links.get_url_site(self.url) 
        self.request = request # 抓取请求体
        self.raw_text = response["text"] # 抓取返回体页面
        self.json = None  # json 
        self.soup = None # css selector 
        self.etree = None # xpath 
        self.container = {}
        self.dir_path = dir_path + 1 # 标记抓取深度标志
    

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
            self.etree = etree.HTML(self.raw_text) 
        return self.etree
