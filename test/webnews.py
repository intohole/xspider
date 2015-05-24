# coding=utf-8
#!/usr/bin/env python
import re


def get_news_json():
    return {'baidu': {'base_url': 'http://news.baidu.com', 'url_rule': [{'tag': 'a', 'attrs': {'target': '_blank'}}] , 'filter' : re.compile('^http://(.*?)(?!baidu)(html|htm)$') }}
