# coding=utf-8


class _BaseQueue(object):

    def __init__(self, queue_len):
        pass

    def get_request(self, *argv, **kw):
        raise NotImplementedError

    def put_request(self, urls):
        raise NotImplementedError


class BaseQueue(object):

    from Queue import Queue

    def __init__(self, queue_len):
        self.queue = Queue()

    def get_request(self, block=True, timeout=None):
        return self.queue.get(block=block, timeout=timeout)

    def put_request(self, urls, block=True, timeout=None):
        return self.queue.put(urls, block=block, timeout=timeout)

    def __len__(self):
        return len(self.queue)


class _CrawledQueue(object):

    """已抓队列实现
    add_urls    #添加已抓链接到已抓队列中
    exist       #判断是否是已抓链接
    """

    def __init__(self, queue_len):
        pass

    def add_urls(self, urls):
        raise NotImplementedError

    def exist(self, urls):
        raise NotImplementedError


class CrawledQueue(object):

    def __init__(self, queue_len):
        self.url_set = set()

    def __getitem__(self, key):
        if key and key in self.url_set:
            return True
        return False

    def __len__(self):
        return len(self.url_set)
