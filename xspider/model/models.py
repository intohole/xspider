# coding=utf-8
from fileds import Fileds

class ZRequest(Fileds):


    def __init__(self, url ,*argv ,**kw):
        super(ZRequest , self).__init__(*argv , **kw)
        self["url"] = url
        self["method"] = kw.get("method" , "GET").lower() 
        self["params"] = kw.get("params" , {})
        
         

class ZResponse(Fileds):


    def __init__(self, url , *argv , **kw):
        super(ZResponse , self).__init__(*argv , **kw)
        self["url"] = url
        self["request"] = kw.get("request" , ZRequest(url))
        self["status_code"] = kw.get( "status_code"  , -1 )
        self["text"] = kw.get("text" , "None") 
