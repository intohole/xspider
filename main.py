#coding=utf-8



from subprocess import call
from collections import defaultdict
import json 
import os
from config import get_config
import time
import re
from doc import Doc
from vampire.utils import network  
from vampire.htmlextract import HtmlExtract  
from lxml import etree



MAIN_CONFIG = get_config()

class UrlFilter(object):


    def __init__(self , urls_file = None):
        self.urls_file = urls_file
        self.load(urls_file)

    def __contains(self , url):
        if not isinstance(url  , unicode ):
            url = url.decode('utf-8')
        if self.urls.has_key(unicode(url)):
            return True
        return False


    def __getitem__(self , key):
        if key:
            return self.__contains(key)
        return False

    def load(self , urls_file):
        self.urls = {}
        if os.path.isfile(urls_file):
            with open(urls_file) as f:
                self.urls = json.loads(f.readline().strip().encode('utf-8'))

    def save(self):
        with open(self.urls_file , 'w') as f:
            f.write(json.dumps(self.urls).encode('utf-8'))



url_filter = UrlFilter('/home/lixuze/urls')



class HtmlTree(object):

    def __init__(self , html):
        self.tree = None
        if html:
            self.tree =  etree.HTML(html.decode('utf-8'))

class BaseSpider(object):
    extract = HtmlExtract()



    def __init__(self  , ml):
        self.main_page = ml


    def extract_url(self , tree , url_rule = 'a'):
        urls = []
        status = False
        if tree is not None:
            if tree is not None:
                for url in tree.xpath( url_rule):
                    urls.append(self.abs_url(url.attrib['href']))
        urls.reverse() #网址下载下来是顺序的　但是抓取的时候是最晚的一个在最前面
        return urls

    def down_html(self , url , code = None):
        return network.get_html_string(url)

    def abs_url(self , url):
        return url

    def get_title(self , tree , title_rule = '//head//title'):
        if tree:
            return tree.xpath(title_rule)

def save_doc(doc ,  file_name ,doc_path = MAIN_CONFIG['doc_path'] ):
    if not file_name:
        return 
    if doc and isinstance(doc , Doc):
        with open('%s%s.md' % (doc_path , file_name) , 'w') as f:
            f.write(str(doc))




class Kr36(BaseSpider):

    def __init__(self):
        self.__pattern = {}
        BaseSpider.__init__(self , 'http://www.36kr.com/')
    



    def run(self ):
        main_html = self.down_html(self.main_page)
        main_tree = HtmlTree(main_html)
        if not url_filter[self.main_page]:
            url_filter.urls[self.main_page] = {}
            url_filter.urls[self.main_page]['cr'] = long(time.time() * 1000)
        url_filter.urls[self.main_page]['fr'] = long(time.time() * 1000)
        for url in self.extract_url(main_tree.tree , url_rule = '//h1//a'):
            if not  url_filter[url]:
                url_filter.urls[url] = {}
                url_filter.urls[url]['cr'] = long(time.time() * 1000)
                html  =  self.down_html(url)
                child_tree = HtmlTree(main_html)

                doc = Doc(self.get_title(html) , self.make_content(self.extract.get_text(html)) , 'li' , 'computer'  , self.get_keywords(html))
                save_doc(doc , doc.file_name )
            else:
                url_filter.urls[url]['fr'] = long(time.time()* 1000)

    def abs_url(self , url):
        return '%s%s'.strip() % (self.main_page[:-1] , url )




    def __get_meta_info(self , html , name):
        pattern = re.compile('<meta name="%s" content=\"(.*?)\"' % name)
        match = pattern.search(html)
        if match:
            return match.group(1)
        return None
        
    def get_title(self , html):
        return self.__get_meta_info( html,'twitter:title')


    def get_keywords(self , html):
        return self.__get_meta_info(html , 'keywords').split(',')


    def make_content(self , html):
        pattern = re.compile(u'\\[(.*?)作者(.*?)\\]')
        if html:
            return pattern.sub( '', html.decode('utf-8') )

        



from utils import make_html
if __name__ == '__main__':
    t = Kr36()
    t.run()
    url_filter.save()
    make_html(MAIN_CONFIG['html_base'])

    # url_filter.save()