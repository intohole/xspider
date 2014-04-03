# coding=utf-8
#!/usr/bin/env python


from BeautifulSoup import BeautifulSOAP
from vampire.utils import network
from webnews import get_news_json
from vampire.htmlextract import HtmlExtract


class Mosquito(object):

    __news__ = get_news_json()
    __extract = HtmlExtract()

    def __getattr__(self, key):
    	urls = []
    	__url_set = set()
        if self.__news__.has_key(key):
            if self.__news__[key].has_key('base_url'):
                html = network.get_html_string(self.__news__[key]['base_url'])
                soup = BeautifulSOAP(html)
                if soup:
                	__filter = self.__news__[key].has_key('filter')
                	for __rule in self.__news__[key]['url_rule']:
                		for __child in soup.findAll(__rule ['tag'] , attrs = __rule['attrs']):
                			__url = __child.get('href')
                			if __url in __url_set:
                				continue
                			__url_set.add(__url)
                			if __filter:
                				if self.__news__[key]['filter'].match(__url):

                				    urls.append(__url)
                			else:
                				urls.append(__url)
        return urls

    def extract(self , url ):
    	if url and len(url) > 0 and url[:4] == 'http':
    		html_string = network.get_html_string(url)
    		return {'content' :self.__extract.get_text(html_string)}
if __name__ == '__main__':

    m = Mosquito()
    print m.extract(m.baidu[1])['content']
