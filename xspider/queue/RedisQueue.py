#coding=utf-8




from redis import Redis
from rq import Queue
from SpiderQueue import BaseQueue 



class RedisQueue(BaseQueue):
    

    def __init__(self,queue_len):
        super(RedisQueue,self).__init__(queue_len)
        self.queue = Queue(connection = Redis())
        
