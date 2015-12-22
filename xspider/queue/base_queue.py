# coding=utf-8

from gevent import queue
from b2.object2 import Singleton
from ..model.models import ZRequest 


class _BaseQueue(object):

    def __init__(self, queue_len):
        pass

    def get_request(self, *argv, **kw):
        raise NotImplementedError

    def put_request(self, urls):
        raise NotImplementedError


class BaseQueue(_BaseQueue):

    def __init__(self, queue_len):
        self._queue = queue.Queue(maxsize=queue_len)

    def get_request(self, block=True, timeout=None):
        return self._queue.get(block=block, timeout=timeout)

    def put_request(self, urls, block=True, timeout=None):
        return self._queue.put(urls, block=block, timeout=timeout)

    def __len__(self):
        return self._queue.qsize()

class DumpSetQueue(BaseQueue):


    def __init__(self , maxsize  = 0, *argv , **kw):
        super(DumpSetQueue , self).__init__(maxsize)
        self.crawled = set()
    
    def put_request(self , request, block = True , timeout = None):
        url = request["url"] if isinstance(request , ZRequest) else request
        if url in self.crawled:
            return False
        self.crawled.add(url)
        self._queue.put(request, block = block , timeout = timeout )
        return True

    def empty(self):
        return self._queue.empty()
