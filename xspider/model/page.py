#coding=utf-8

from ..selector.css_selector import CssSelector 


class Page(object):



    def __init__(self ,request , response ):
        self.request = request
        self.json = None 
        self.raw_text = response["text"]
        self.soup = None 
        self.container = {}
    

    def css(self):
        if self.soup is None:
            self.soup = CssSelector(self.raw_text)
        return self.soup.soup

