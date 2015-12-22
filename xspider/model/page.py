#coding=utf-8




class Page(object):



    def __init__(self , response ):
        self.json = None 
        self.html = response["text"]
