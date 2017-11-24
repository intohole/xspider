xspider部分api
========


创建爬虫
-------
+ 爬虫
    + BaseSpider
        - BaseSpider(name,*argv,**kw)
        - name 爬虫名称
        - log_level 爬虫日志级别，默认warn
        - allow_site list类型，运行爬虫的站点
        - start_urls list类型，种子链接
        - page_processor PageProcessor类型，抽取器
        - fetcher 抓取器，默认BaseRequestsFetcher()
        - pipeline 处理管道,默认终端管道
        - queue 抓去队列，默认MemoryFifoQueue(10000),内存先进先出队列
        - url_filters 链接过滤器list，默认［］
        - listeners 爬虫抓取动作,默认 [DefaultSpiderListener()]
        - crawled_filter 已经抓取链接过滤器，默认为None，不对已经抓取的链接进行过滤
+ 抽取
    + PageProcessor
        - process(self,page,spider)
            - 处理页面
    + PageMatchStartUrlPrcocessor
        - BasePageMatchUrlProcessor(name,url_pattern,lower=True)
            - name 抽取器名称
            - url_pattern 链接前缀,字符串类型
            - lower 是否忽略大小写，默认为True
    + PageMatchEndUrlPrcocessor
        - BasePageMatchUrlProcessor(name,url_pattern,lower=True)
            - name 抽取器名称
            - url_pattern 链接后缀,字符串类型
            - lower 是否忽略大小写，默认为True 
+ 管道
    + ConsolePipeLine
        - 
+ 过滤器
+ 队列
+ 选取器
