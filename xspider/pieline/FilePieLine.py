#coding=utf-8




class FilePie(PieLine):


    def __init__(self ,**kw):
        super(FilePie , self).__init__()
        self.folder_path = kw.get("folder_path" , None)
        if self.folder_path is None or isinstance(self.folder_path , basestring):
            raise ValueError
        self.spider = kw.get("spider" , None) 
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
        self.map_file_handle.write("{write_path}\t{url}".format(write_path = write_path , url = item["request"]["url"])
    
    def destory(spider):
        self.map_file_handle.close()
