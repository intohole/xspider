#coding=utf-8


from PipeLine import PipeLine
import os
from b2 import file2 

__all__ = ["FilePipe"]

class FilePipe(PipeLine):
    """文件管道
        Test:
            >>> from xspider.spider import BaseSpider
            >>> spider = BaseSpider()
            >>> 
    """


    def __init__(self ,**kw):
        super(FilePipe , self).__init__()
        self.folder_path = kw.get("folder_path" , "./data")
        if not isinstance(self.folder_path , basestring):
            raise TypeError("Unsupported type {}".format(type(folder_path).__name__)) 
        self.spider = kw.get("spider" , None)
        if self.spider is None or not ( hasattr( self.spider , "spid") and isinstance(getattr(self.spider , "spid") , basestring)):
            raise ValueError("get not valueable spid attr")
        self.work_folder = os.path.join(self.folder_path ,self.spider.spid)
        file2.mkdir_p(os.path.join(self.work_folder , "data"))
        self.map_file = kw.get("map_file" ,os.path.join(self.work_folder ,"map.result") )
        self.map_file_handle = open(self.map_file , "a")


    def excute(self , item , spider):
        if item is None:
            return False
        write_path = os.path.join(self.work_folder,spider.count)
        filehandle = open(write_path , "w")
        filehandle.write("%s\n" % str(item))
        filehandle.close()
        self.map_file_handle.write("{write_path}\t{url}".format(write_path = write_path , url = item["request"]["url"]))


    def destory(self,spider):
        self.map_file_handle.close()
