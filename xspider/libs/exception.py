#coding-utf-8



class SpiderException(Exception):
    """xspider异常定义类
        try:
            int("1212s")
        except:
            raise SpiderException("input type must be in [int,long]")
    """

    def __init__(self ,msg):
        super(SpiderException , self).__init__()
        self.msg = msg

    def __str__(self):
        return "error :[{error}]".format(error = self.msg)
