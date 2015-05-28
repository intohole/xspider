# coding=utf-8


import threading


class Singleton(object):

    """python单例实现方式
    """
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            mutex = threading.Lock()
            mutex.acquire()
            if not hasattr(cls, '_instance'):
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
            mutex.release()
        return cls._instance



