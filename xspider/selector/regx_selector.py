#coding=utf-8




#from selector import Selector 
import re


class RegxSelector(object):



    def __init__(self , regx):
        self.pattern = re.compile(regx)    
        
    def finds(self , page):
        """从raw_text找到,定义正则表达式内容
            params:
               page                 网页下载后结构体
            return 
                []                  正则抽取出的item
            raise 
                None
            test:
                >>> r = RegxSelector("[0-9]{1,}")
                >>> print r.finds("12a45b")
        """
        return [group for group in self.pattern.findall(page)]

    def find(self , page):
        group = self.pattern.match(page.raw_text)
        if group:
            return group.group()
        return None 

