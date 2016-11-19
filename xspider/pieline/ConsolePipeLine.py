#coding=utf-8





from PipeLine import PipeLine
import sys
import json

class ConsolePipeLine(PipeLine):
    """spider consle output
    """

    def __init__(self , *argv , **kw):
        self.stdout = kw.get("stdout" , sys.stdout)

    def process(self , item):
        self.stdout.write("%s\n"  % json.dumps(item))

    def destroy(self , item , spider):
        self.stdout.close()
