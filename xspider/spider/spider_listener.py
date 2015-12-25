#coding=utf-8


import spider as spiderman

class SpiderListener(object):


    def spider_stop(self , spider):
        raise NotImplmentError

    def spider_start(self , spider):
        raise NotImplmentError




class DefaultSpiderListener(object):
    """爬虫各种状态的监听者，监听者模式
        test:
            >>> sl = DefaultSpiderListener(BaseSpider("12312"))
            >>> sl.spider_stop(self , spider)
    """


    def spider_stop(self , spider):
        if spider and isinstance(spider , spiderman.BaseSpider) and hasattr(spider , "pielines"): 
            pielines = getattr(spider , "pielines")
            for pieline in pielines:
                pieline.destory()
    

    def spider_start(self , spider):
        pass
