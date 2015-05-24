#coding=utf-8




class BaseQueue(object):



    def __init__(self , queue_len ):
        pass


    def get_request(self , *argv , **kw):
        raise NotImplementedError


class CrawledQueue(object):
    """已抓队列实现
    add_urls    #添加已抓链接到已抓队列中
    exist       #判断是否是已抓链接
    """


    def __init__(self , queue_len ):
        pass



    def add_urls(self , urls):
        raise NotImplementedError



    def exist(self , urls):
        raise NotImplementedError



