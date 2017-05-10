#coding=utf-8



import unittest
from xspider.selector import css_selector
from xspider.model import page
from xspider.model import models 
import requests

class TestBloomCrawledFilter(unittest.TestCase):
    
   
        
    def test_chijiuhua(self):
        url = "https://githuber.cn/search?location=china"
        response = requests.get(url)
        request = models.ZRequest(url,1) 
        response = models.ZResponse(url,text=response.text)
        pageModel = page.Page(request,response,1)
        for i in pageModel.get_soup().select("a[href]"):
            print i["href"]
        extracotor = css_selector.CssSelector(tag = "a", attr = "href")
        for link in extracotor.finds(pageModel):
            print link
    
if __name__ == '__main__':
    unittest.main()
