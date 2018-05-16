#coding=utf-8

import spider as spiderman

__ALL__ = ["SpiderListener", "Listener", "DefaultSpiderListener"]


class SpiderListener(object):
    def __init__(self):
        self.listerners = {}

    def addListener(self, listener):
        if listener and isinstance(listener, Listener):
            self.listerners[id(listener)] = listener
            return id(listener)
        elif listener and isinstance(listener, (list, tuple)):
            for _listerner in listener:
                self.addListener(_listerner)
        return False

    def removeListener(self, listern_id):
        if listern_id and listern_id in self.listerners:
            del self.listerns[listern_id]
            return True
        return False

    def notify(self, msg, spider):
        for listener in self.listerners.values():
            listener.notify(msg, spider)


class Listener(object):
    def notify(self, msg):
        raise NotImplmentError


class DefaultSpiderListener(Listener):
    """爬虫各种状态的监听者，监听者模式
        test:
            >>> sl = DefaultSpiderListener(BaseSpider("12312"))
            >>> sl.spider_stop(self , spider)
    """

    def spider_stop(self, spider):
        if spider and isinstance(spider, spiderman.BaseSpider):
            if hasattr(spider, "pielines"):
                pielines = getattr(spider, "pielines")
                for pieline in pielines:
                    pieline.destory(spider)
            if hasattr(spider, "url_pool"):
                url_pool = getattr(spider, "url_pool")
                if url_pool and hasattr(url_pool, "close"):
                    url_pool.close()
            spider.logger.error("spider has colsed")

    def spider_start(self, spider):
        pass

    def notify(self, msg, spider):
        if hasattr(self, msg) and callable(getattr(self, msg)):
            getattr(self, msg)(spider)
