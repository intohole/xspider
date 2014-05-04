# coding=utf-8
#!/usr/bin/env python


from BeautifulSoup import BeautifulSoup
from vampire.utils import network
from webnews import get_news_json
from vampire.htmlextract import HtmlExtract
import re


class Mosquito(object):

    __title = re.compile(u'<[ ]{0,}title[ ]{0,}>(.*?)<[ ]{0,}/tilte[ ]{0 ,}>' , re.I)
    __news__ = get_news_json()
    __html_extract = HtmlExtract()

    def __getattr__(self, key):
        content = []
        __url_set = set()
        if self.__news__.has_key(key):
            if self.__news__[key].has_key('base_url'):
                print 'download......'
                html = network.get_html_string(self.__news__[key]['base_url'])
                print 'download finish .....'
                soup = BeautifulSoup(html)
                # print html
                if soup:
                    print 'x'
                    __filter = self.__news__[key].has_key('filter')
                    for __rule in self.__news__[key]['url_rule']:
                        for __child in soup.findAll(__rule['tag'], attrs=__rule['attrs']):
                            __url = __child.get('href')
                            if __url in __url_set:
                                continue
                            __url_set.add(__url)
                            if __filter:
                                if self.__news__[key]['filter'].match(__url):
                                    content.append(self.__extract(__url))
                            else:
                                content.append(self.__extract(__url))
        return content

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __get_title(self, soup):
        if soup:
            return soup.title.string
        return None

    def __extract(self, url):
        if url and len(url) > 0 and url[:4] == 'http':
            try:
                news = {}
                html_string = network.get_html_string(url)
                soup = BeautifulSoup(html_string)
                news['title'] = self.__get_title(soup)
                content = self.__html_extract.get_text(html_string)
                news['content'] = content
                # news['title'] = self.__extract_title(html_string)
                print news
                return news
            except Exception, e:
                print e
        return None

    def __extract_title(self, html):
        if html and html != '':
            if isinstance(html, (str, unicode)):
                 print html
                 m = self.__title.search(html)
                 print 'm'
                 print m
                 if m:
                    print 'title'
                    return m.group(0)
        return None

if __name__ == '__main__':

    m = Mosquito()
    print m['baidu']
    print 'get....'
