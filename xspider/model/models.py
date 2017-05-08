#coding=utf-8
from fileds import Fileds
import time
import json

class ZRequest(Fileds):


    def __init__(self, url  , dir_path ,*argv ,**kw):
        super(ZRequest , self).__init__(*argv , **kw)
        self["url"] = url
        self["method"] = kw.get("method" , "GET").lower() 
        self["params"] = kw.get("params" , {})
        self["headers"] = kw.get("headers" , {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
        self["dir_path"] = dir_path + 1 
         
    def dumps(self):
        return json.dumps(self)           
    
    @staticmethod
    def loads(value):
        """通过字符串加载对象，通过字符串序列化
            param:value:basestring:反序列化字符串
            return:ZRequest:ZRequest:返回反序列化对象
            Test:
                >>> request = ZRequest("www.baidu.com",0)
                >>> j = request.dumps()
                >>> r = ZRequest.loads(j)
                >>> print r
                {"url": "www.baidu.com", "headers": {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}, "params": {}, "method": "get", "dir_path": 2}
        """
        d = json.loads(value)
        url = d["url"]
        dir_path = d["dir_path"]
        del d["url"]
        del d["dir_path"]
        return ZRequest(url,dir_path,**d)
        
        

class ZResponse(Fileds):


    def __init__(self, url , *argv , **kw):
        super(ZResponse , self).__init__(*argv , **kw)
        self["url"] = url
        self["request"] = kw.get("request" , ZRequest(url , -1))
        self["status_code"] = kw.get( "status_code"  , -1 )
        self["text"] = kw.get("text" , "None") 
        self["headers"] = kw.get("header" , {})
        self["crawl_time"] = kw.get("crawl_time" , time.time())
