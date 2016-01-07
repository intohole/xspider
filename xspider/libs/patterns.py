#coding=utf-8

import links 
import urlparse





class _Pattern(object):



    def __init__(self , pattern_dict):
        pass




    def _split_url_item(self , url):
        return urlparse.urlparse(url)

    def _translate_url_item(self , items ):
        netloc , path , params , query , fragment = items
        paths = path.split("/")
        for path_item in paths:
            path_item

    def __call__(self , url):
        pass
