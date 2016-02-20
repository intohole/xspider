#coding=utf-8
"""基于redis实现队列方式，将爬虫变为可分布式的爬虫;
    pip install redis 
"""



import redis



class RedisQueue(object):

    def __init__(self , maxsize = 0 , *argv , **kw):
        super(RedisQueue , self).__init__(maxsize)
        host = kw.get("host" , "localhost")
        port = kw.get("port" , "6379")
        db = kw.get("db" , "0")
        self.db = redis.Redis(host = host , port = port  , db = db )
        self.crawled()


    def put_requests(self , request):
        pass
