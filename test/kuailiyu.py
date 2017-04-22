#coding=utf-8




from xspider import processor
from xspider.selector import xpath_selector
from xspider import model

class KuaiLiYu(processor.PageProcessor.PageProcessor):


    def __init__(self):
        super(KuaiLiYu , self).__init__()
        self.title_extractor = xpath_selector.XpathSelector(path = "//title/text()")

    def process(self , page , spider):
        items = model.fileds.Fileds()
        items["title"] = self.title_extractor.find(page)
        items["url"] = page.url
        return items

