# coding=utf-8
from Fileds import Fileds

class Request(Fileds):

    __slots__ = ('url' , "method" , "params")

    def __init__(self, url ,**kw):
        self.url = url
        self.method = getdefault(kw , "method" , "GET").lower() 
        self.params = getdefault(kw , "params" , {})
        
         

class Response(object):

    __slots__ = ('body', 'url', 'status')

    def __init__(self, url, status_code, text):
        self.url = url
        self.status_code = status_code
        self.text = text 
