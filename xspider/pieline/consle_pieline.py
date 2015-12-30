#coding=utf-8





from PieLine import PieLine
import sys


class ConslePieLine(PieLine):
    """终端输出
    """

    def __init__(self , *argv , **kw):
        self.stdout = kw.get("stdout" , sys.stdout)
    
    def process(self , item):
        self.stdout.write("%s\n"  % item)
    
    def destroy(self , item , spider):
        self.stdout.close()
