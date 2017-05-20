#coding=utf-8

from b2 import log2


class Handler(object):
    
    
    
    def __init__(self):
        pass

    
    def handle404(self,request,response):
        pass 



    def handle502(self,request,response):
        pass

    def handleException(self,request,response,e):
        pass






class LogHandler(object):
    


    def __init__(self):
        logger = log2.get_stream_logger("warn")
    
    
    def handle404(self,request,response):
        self.logger.warn("request {} fail , get status code 404".format(request["url"]))



    def handel502(self,request,response):
        self.logger.warn("request {} fail , get status code 502".format(request["url"]))


    def handleException(self,request,response):
        self.logger.warn("request {} fail , get exception  {}".format(request["url"],str(e)))
