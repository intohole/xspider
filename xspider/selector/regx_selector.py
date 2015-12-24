#coding=utf-8




from extractor import Selector 
import re


class RegxSelector(BaseExtractor):



    def __init__(self , regx):
        self.pattern = re.compile(regx)    

    def regx():

