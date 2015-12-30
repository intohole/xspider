#coding=utf-8


from ..model.fileds import Fileds

class PageProcessor(object):



    def process(self , page , spider):
        raise NotImplmentError



class SimplePageProcessor(object):



    def process(self , page ,spider):
        fileds = Fileds()
        fileds["test"] = 12
        return fileds
