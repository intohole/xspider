#coding=utf-8
from b2.stop2 import StopWords

__ALL__ = [ "get_url_site"]

_url_protocls = StopWords(words = ["http://" , "https://"] ) 

def get_url_site(url):
    """得到链接站点 ， 主要是第一个/切分
        params
            url             链接
        return  
            value           提取站点失败后，返回None，否则返回站点字符串       
        return 
            False
        Test:
            >>> get_url_site("http://www.test.com/index.php")
            >>> get_url_site("123.12.21.0:81/look") 
    """
    if url:
        url = url.lower()
        value , msg = _url_protocls.startswith(url)
        url = url[value:] if value else url    
        return url.split("/")[0]
    return None 



def join_url(site , url ,protocl = "http://"):
    """站点进行补全操作
    """
    url_site = get_url_site(url)
    if url_site == "":
        return "{protocl}{site}{url}".format(protocl = protocl ,site = site , url = url)
    value , msg = _url_protocls.startswith(url)
    if value:
        return url
    else:
        return "{protocl}{url}".format(protocl = value , url = url)
    return url
