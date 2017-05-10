#coding=utf-8



import unittest
from xspider.libs import links
import os

class TestBloomCrawledFilter(unittest.TestCase):
    
   
        
    def test_chijiuhua(self):
        self.assertEqual(links.get_url_protocol("https://githuber.cn/search?location=china"),"https://") 
    
if __name__ == '__main__':
    unittest.main()
