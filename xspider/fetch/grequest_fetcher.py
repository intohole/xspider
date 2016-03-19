#coding=utf-8



import grequests
from fetcher import _BaseFetcher 




class GrequestsFetcher(_BaseFetcher):





    def __init__(self):
        super(GrequestsFetcher ,self).__init__()

    def fetch(self , request):
        if request is None:
            self.logger.error("download [%s] is fail" % request)    

