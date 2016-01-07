#coding=utf-8

import requests
from b2.log2 import get_stream_logger 
from ..model.models import ZResponse 




class _BaseFetcher(object):

    """基本抓取器
    get_result      得到链接网页信息
    """

    def __init__(self , log_level = "DEBUG"):
        self.logger = get_stream_logger(log_level) 

    def request(self, urls, method='get', *argv, **kw):
        raise NotImplementedError






class BaseRequestsFetcher(_BaseFetcher):

    def __init__(self):
        super(BaseRequestsFetcher , self).__init__()

    def fetch(self , request):
        if request is None:
            self.logger.error("download [%s] is fail" % request)    
            yield  
        method = getattr(requests ,request["method"])
        response = method(request["url"] , params = request["params"] ,headers = request["headers"])
        if response and response.status_code == requests.codes.ok:
            yield ZResponse(response.url , status_code =  response.status_code , text = response.text) 
    

class GeventFetcher(object):

    def fetch(self,request):
        if request is None:
            self.logger.error("download [%s] is fail" % request)    
            yield
        method = request.get("method" , "get") 
        url = request.get("url" , url)
