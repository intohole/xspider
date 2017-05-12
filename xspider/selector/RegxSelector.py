#coding=utf-8




#from selector import Selector 
import re


class RegxSelector(object):



    def __init__(self , regx):
        self.pattern = re.compile(regx)    
        
    def finds(self , page):
        """从raw_text找到,定义正则表达式内容
         """
        return [group for group in self.pattern.findall(page)]

    def select(self, page):
        """
        """
        pass
