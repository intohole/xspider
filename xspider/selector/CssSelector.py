#coding=utf-8

from selector import Selector
try:
    from bs4 import BeautifulSoup
except:
    from BeautifulSoup import BeautifulSoup


class CssSelector(Selector):
    def __init__(self, css, **kw):
        super(CssSelector, self).__init__("css", **kw)
        self.css = css

    def find(self, page):
        return page.get_soup().select(self.css)
