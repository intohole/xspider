# coding=utf-8

from b2.object2 import Singleton
from ..model.models import ZRequest 
import Queue

class BaseQueue(object):

    def __init__(self, queue_len):
        self._queue_len = queue_len 

    def pop(self, *argv, **kw):
        raise NotImplementedError

    def push(self, urls):
        raise NotImplementedError
    
    def empty(self):
        return len(self) == 0
    
    def colse(self):
        return  

    def full(self):
        if self._queue_len is None:
            return False
        return len(self) >= self._queue_len

class MemoryLifoQueue(BaseQueue):
    """memory queue implement lifo 
    """
    
    def __init__(self, queue_len):
        super(MemoryLIFOQueue,self).__init__(queue_len)
        self._queue = Queue.LifoQueue() if queue_len is None else Queue.LifoQueue(queue) 

    def pop(self,*argv,**kw):
        block = kw.get("block",True) 
        timeout = kw.get("timeout",None)
        return self._queue.get(block = block ,timeout = timeout) 

    def push(self, request,**kw):
        block = kw.get("block",True) 
        timeout = kw.get("timeout",None)
        return self._queue.put(request, block=block, timeout=timeout)

    def __len__(self):
        return self._queue.qsize()
    

class MemoryFifoQueue(BaseQueue):
    """memory first input first output queue
    """

    def __init__(self,queue_len):
        super(MemoryFifoQueue,self).__init__(queue_len)
        self._queue = Queue.Queue() if queue_len else Queue.Queue(queue_len) 
    
    def pop(self,*argv,**kw):
        block = kw.get("block",True) 
        timeout = kw.get("timeout",None)
        return self._queue.get(block = block ,timeout = timeout) 

    def push(self, request,**kw):
        block = kw.get("block",True) 
        timeout = kw.get("timeout",None)
        return self._queue.put(request, block=block, timeout=timeout)

    def __len__(self):
        return self._queue.qsize()
