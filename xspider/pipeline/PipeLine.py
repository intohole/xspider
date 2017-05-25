#coding=utf-8


from b2 import file2
import os



class PipeLine(object):

    def __init__(self,name = None):
        self.name = name if name is not None else type(self).__name__

    def process(self , page):
        pass

    def destory(self , spider):
        pass

