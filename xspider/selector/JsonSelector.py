#coding=utf-8

from selector import Selector
from b2.json2 import JPath
from b2 import exceptions2


class JsonSelector(Selector):
    """json xpath selector
    """

    def __init__(self, **kw):
        super(JsonSelector, self).__init__("json", **kw)
        self.query = kw.get("query", None)
        exceptions2.judge_null(self.query)
        self.jpath = JPath(self.query)

    def find(self, page):
        if self.query:
            return self.jpath.extract(page.get_json())
