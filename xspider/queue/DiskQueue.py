#coding=utf-8


from base_queue import BaseQueue
from b2.queue2 import FifoDiskQueue 
from b2.queue2 import LifoDiskQueue
from ..model.models import ZRequest


class SpiderFifoDiskQueue(BaseQueue):
    """基于文件队列，不保证线程安全
    """ 
    
    
    def __init__(self,save_folder,chunk_size,queue_len = None):
        super(SpiderFifoDiskQueue,self).__init__(queue_len)
        self.chunk_size = chunk_size
        self.save_folder = save_folder
        self.queue = FifoDiskQueue(save_folder,chunk_size)

    
    def pop(self,*argv,**kw):
        return ZRequest.loads(self.queue.pop())
        
    
    def push(self,request):
        self.queue.push(request.dumps())
    
    def __len__(self):
        return len(self.queue)

    def empty(self):
        return len(self) == 0
    
    def close(self):
        self.queue.close()



class SpiderLifoDiskQueue(BaseQueue):
    """文件队列实现了后入先出
    """

    def __init__(self,queue_file,queue_len = None):
        super(SpiderLifoDiskQueue,self).__init__(queue_len) 
        self._queue = LifoDiskQueue(queue_file)
    
    
    def pop(self,*argv,**kw):
        return ZRequest.loads(self._queue.pop())
    
    def push(self,request):
        self._queue.push(request.dumps())
    
    def __len__(self):
        return len(self._queue)

    def empty(self):
        return len(self) == 0
    
    def close(self):
        self._queue.close()
