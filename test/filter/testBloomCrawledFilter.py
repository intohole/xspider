#coding=utf-8



import unittest
from xspider.filters import BloomCrawledFilter
import os

class TestBloomCrawledFilter(unittest.TestCase):
    
    def setUp(self):
        self.bloom_file = ".bloom_tmp_file"
    
        
    def test_chijiuhua(self):
        bloom = BloomCrawledFilter.BloomCrawledFilter(self.bloom_file,1000)
        self.assertFalse(bloom.filter("https://buyiker.com"))
        self.assertTrue(bloom.filter("https://buyiker.com"))
        bloom1 = BloomCrawledFilter.BloomCrawledFilter(self.bloom_file,1000)
        self.assertTrue(bloom1.filter("https://buyiker.com"))
    
    def tearDown(self):
        if os.path.exists(self.bloom_file):
            os.remove(self.bloom_file)

if __name__ == '__main__':
    unittest.main()
