#coding=utf-8


from ..model.fileds import Fileds

class PageProcessor(object):



    def extract(self , page):
        raise NotImplmentError



class SimplePageProcessor(object):



    def extract(self , page):
        fileds = Fileds()
        fileds["test"] = 12
        return fileds
