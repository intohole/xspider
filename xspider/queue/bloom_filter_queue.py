#coding=utf-8


from pybloomfilter import BloomFilter
from base_queue import BaseQueue 

class BloomFilterQueue(BaseQueue):



    def __init__(self , bloomfilter_path ,capacity , wrong_rate , maxsize , *argv , **kw):
        super(BloomFilterQueue , self).__init__(maxsize)
        self.crawled = BloomFilter(capacity  , wrong_rate , bloomfilter_path)

    def put_request(self , request , block = True , timeout = None ):
        url = request["url"] if isinstance(request ,ZRequest ) else request
        if url in self.crawled:
            return False
        self.crawled.add(url)
        self._queue.put(request , block = block , timeout = timeout)
