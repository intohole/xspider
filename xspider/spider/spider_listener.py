#coding=utf-8


from spider import BaseSpider 

class SpiderListener(object):


    def spider_stop(self , spider):
        raise NotImplmentError

    def spider_start(self , spider):
        raise NotImplmentError




class DefaultSpiderListener(object):



    def spider_stop(self , spider):
        if spider and isinstance(spider , BaseSpider) and hasattr(spider , "pielines"): 
            pielines = getattr(spider , "pielines")
            for pieline in pielines:
                pieline.destory()
    

    def spider_start(self , spider):
        pass
