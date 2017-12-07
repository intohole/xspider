#coding=utf-8

from PipeLine import PipeLine
import os
from b2 import file2
from b2 import exceptions2
import json
import hashlib
from b2 import rand2

__all__ = ["FilePipe", "DumpFilePipe"]


class FilePipe(PipeLine):
    """文件管道
        Test:
            >>> from xspider.spider import BaseSpider
            >>> spider = BaseSpider()
            >>>
    """

    def __init__(self, **kw):
        super(FilePipe, self).__init__()
        self.folder_path = kw.get("folder_path", "./data")
        if not isinstance(self.folder_path, basestring):
            exceptions2.raiseTypeError(self.folder_path)
        self.work_folder = os.path.join(self.folder_path)
        self.map_file = kw.get("map_file",
                               os.path.join(self.work_folder, "map.result"))
        self.map_file_handle = open(self.map_file, "a")
        self._md5 = hashlib.md5()

    def excute(self, item):
        url = item["request"]["url"]
        md5 = self._md5.update(url).hexdigest()
        with open(os.path.join(self.work_folder, md5), "w") as f:
            f.write(json.dumps(item))
        self.map_file_handle.write("{write_path}\t{url}".format(
            write_path=write_path, url=url))

    def destory(self, spider):
        self.map_file_handle.close()


class DumpFilePipe(PipeLine):
    """只会将文件保存在一个文件中，将所有item序列化成json后处理
    """

    def __init__(self, **kw):
        super(DumpFilePipe, self).__init__()
        self._file = kw.get("file", "%s.txt" % rand2.get_random_seq(10))
        self._mode = kw.get("mode", "w")
        self._file_handle = open(self._file, self._mode)

    def process(self, item):
        self._file_handle.write("%s\n" % json.dumps(item))

    def destroy(self, item, spider):
        self._file_handle.close()
