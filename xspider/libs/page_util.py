#coding=utf-8

from b2 import exceptions2
import re
import chardet


def get_html_charset(html):
    """get html charset/encoding
        this is easy way to use chardet detect html encoding
    """
    if html is None:
        return None
    exceptions2.judge_type(html, basestring)
    return chardet.detect(self.content)['encoding']
