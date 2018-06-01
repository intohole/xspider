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

    def get_text(self, page, index=0):
        contents = self.find(page)
        if contents is not None and len(contents) > index:
            return contents[0].text
        return None

    def get_texts(self, page):
        contents = self.find(page)
        if contents is not None and len(contents) > 0:
            return [content.text for content in contents]
        return []

    def get_html(self, page, index=0):
        contents = self.find(page)
        if contents is not None and len(contents) > index:
            return str(contents[index])
        return None

    def get_table(self, page, tag):
        contents = self.find(page)
        if contents is not None and len(contents) > index:
            for content in contents:
                kv = content.select(tag)
                yield kv[0].text, kv[1].text
        return []
