# coding=utf-8
#!/usr/bin/env python


from BeautifulSoup import BeautifulSOAP
from vampire.utils import network
from webnews import get_news_json
from vampire.htmlextract import HtmlExtract


class Mosquito(object):

    __news__ = get_news_json()
    __html_extract = HtmlExtract()

    def __getattr__(self, key):
        urls = []
        __url_set = set()
        if self.__news__.has_key(key):
            if self.__news__[key].has_key('base_url'):
                print 'download......'
                html = network.get_html_string(self.__news__[key]['base_url'])
                print 'download finish .....'
                soup = BeautifulSOAP(html)
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
                                    urls.append(self.__extract(__url))
                            else:
                                urls.append(self.__extract(__url))
        return urls

    def __getitem__(self, key):
        return self.__getattr__(key)


    def __get_title(self , soup):
        if soup :
            return soup.head.title.string
        return None
    def __extract(self, url):
        if url and len(url) > 0 and url[:4] == 'http':
            try:
                news = {}
                html_string = network.get_html_string(url)
                soup = BeautifulSOAP(html_string)
                news['title'] = self.__get_title(soup)
                content = self.__html_extract.get_text(html_string)
                news['content'] = content 
                return 
            except Exception, e:
                print e
        return None


if __name__ == '__main__':

    m = Mosquito()
    print m['baidu']
    print 'get....'
