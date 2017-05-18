#coding-utf-8



class BaseException(Exception):
    """xspider异常定义类
        try:
            int("1212s")
        except:
            raise SpiderException("input type must be in [int,long]")
    """

    def __init__(self ,msg):
        super(BasException , self).__init__()
        self.msg = msg

    def __str__(self):
        return "error :[{error}]".format(error = self.msg)


class URLException(BaseException):
    """Raise this when a URL is illegal"""
    pass

class SpiderException(BaseException):
    """Old exception"""
    pass

class CloseSpider(BaseException):
    """Raise this from callbacks to request the spider to be closed"""

    def __init__(self, reason='cancelled'):
        super(BaseSpider, self).__init__()
        self.reason = reason
