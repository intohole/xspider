# coding=utf-8
from fileds import Fileds
import time

class ZRequest(Fileds):


    def __init__(self, url ,*argv ,**kw):
        super(ZRequest , self).__init__(*argv , **kw)
        self["url"] = url
        self["method"] = kw.get("method" , "GET").lower() 
        self["params"] = kw.get("params" , {})
        self["headers"] = kw.get("headers" , {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
         
         

class ZResponse(Fileds):


    def __init__(self, url , *argv , **kw):
        super(ZResponse , self).__init__(*argv , **kw)
        self["url"] = url
        self["request"] = kw.get("request" , ZRequest(url))
        self["status_code"] = kw.get( "status_code"  , -1 )
        self["text"] = kw.get("text" , "None") 
        self["headers"] = kw.get("header" , {})
        self["crawl_time"] = kw.get("crawl_time" , time.time())
