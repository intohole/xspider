xspider 简单python抓取框架
============



xspider
----------------
+ 抓取单线程
+ 简单api使用
+ xpath/css/json提取器
+ 多种队列
+ 架构代码逻辑清晰，可以了解spider抓取过程
+ it's easy to crawl and extract web;


:::python 

	main.py:
	
		from xspider.spider.spider import BaseSpider
		from xspider.filters import urlfilter
		from kuailiyu import KuaiLiYu

	if __name__ == "__main__":
    	spider = BaseSpider(name = "kuailiyu"  , page_processor = KuaiLiYu() , allow_site = ["kuailiyu.cyzone.cn"] , start_urls = ["http://kuailiyu.cyzone.cn/"])
    	spider.url_filters.append(urlfilter.UrlRegxFilter(["kuailiyu.cyzone.cn/article/[0-9]*\.html$","kuailiyu.cyzone.cn/index_[0-9]+.html$"]))
    	spider.start()

	kuailiyu.py
		from xspider import processor 
		from xspider.selector import xpath_selector
		from xspider import model


		class KuaiLiYu(processor.PageProcessor.PageProcessor):


    		def __init__(self):
        		super(KuaiLiYu , self).__init__()
        		self.title_extractor = xpath_selector.XpathSelector(path = "//title/text()")

    		def process(self , page , spider):
        		items = model.fileds.Fileds()
        		items["title"] = self.title_extractor.find(page)
        		items["url"] = page.url
        		return items

			



抓取部分有以下工程代码
==========
+ [PhantomjsFetcher](https://github.com/2shou/PhantomjsFetcher)
+ [pyspider](https://github.com/binux/pyspider)
