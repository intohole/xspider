xspider部分api
========


创建爬虫
-------
+ 爬虫
    + xspider.spider.spider.BaseSpider
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
    + xspider.pipeline.ConsolePipeLine.ConsolePipeLine
        - 将解析内容直接输出到终端下
    + xspider.pipeline.FilePipeLine.FilePipe
        - 参数
            - folder_path 保存文件夹，默认值./data
        - 将解析内容直接保存到文件中，并且内容是json形式
+ 过滤器
    + 过滤器基础方法
        - set_must_check()
            - 设置后，必需强制满足，如果不满足，直接过滤
        - set_priority()
            - 设置过滤器的优先级
    + xspider.filters.UrlFilter.SiteFilter
        - 参数
            - sites 站点集合，list／set类型
        - 如果符合sites站点链接将保留，否则返回false
        
    + xspider.filters.UrlFilter.UrlRegxFilter
        - 参数
            - url_regxs 链接正则list，[正则表达式1，正则表达式2...]
        - 如果链接符合正则表达式保留，正则表达式使用搜索模式

    + xspider.filters.UrlFilter.UrlStartFilter
        - 参数
            - prefix 链接前缀,str类型
        - 如果链接开头符合前缀链接被保留

    + xspider.filters.UrlFilter.UrlEndFilter
        - 参数
            - suffix 链接后缀,str类型
        - 如果链接开头符合后缀链接被保留

    + xspider.filters.UrlFilter.UrlDirPathFilter
        - 参数
            - dir_path_limit 链接保留最大层级
        - 为了避免过深入抓取链接，使用链接层级过滤，注明，使用此过滤器，如果不符合条件，直接链接丢弃，不再处理

    + xspider.filters.UrlFilter.UrlFilterContainer
        - 参数
           - filters 过滤器列表
        - 只有filters所有过滤器都不过滤链接的时候，链接才会保存，相当于所有过滤器做与操作

    + xspider.filters.UrlFilter.CrawledFilter.SimpleCrawledFilter
        - 直接使用set类型作为抓取过滤，如果设置此过滤类型，请注意内存，另外会直接过滤已经抓取链接
    + xspider.filters.UrlFilter.CrawledFilters.BloomCrawledFilter
        - 参数
            - bloom_file 序列化数据保存位置
            - url_size 链接保存的大小
            - error_rate 撞击概率,默认值0.001
        - 使用bloom过滤器，过滤已经抓取的链接，因算法原因，链接有概率被重复抓取，但设置参数可以将概率下降到最低，主要是为了内存较少爬虫使用
+ 队列
    + xspider.queue.DiskQueue.SpiderFifoDiskQueue
        - 参数
            - save_folder 队列序列化位置
            - chunk_size 文件队列单文件保存的条数
            - queue_len 队列最大大小，默认无限制
        - 队列线程不安全，请使用的时候注意，先进先出队列，适合广度搜索

    + xspider.queue.DiskQueue.SpiderLifoDiskQueue
        - 参数
            - queue_file 队列文件
            - queue_len 文件最大存储大小
        - 队列线程不安全，后进先出队列，适合深度搜索

    + xspider.queue.SpiderQueue.MemoryLifoQueue
        - 参数
            - queue_len 队列最大大小
        - 队列线程安全，存储在内存中，后进先出队列，适合深度搜索

    + xspider.queue.SpiderQueue.MemoryFifoQueue
        - 参数
            - queue_len 队列最大大小
        - 队列线程安全,存储在内存中，先进先出队列，适合广度搜索

+ 选取器
    + xspider.selector.CssSelector.CssSelector
        - 参数
            - css css选取器字符串
        - 通过生成规则，对html进行解析
    + xspider.selector.JsonSelector.JsonExtractor
        - 参数
            - paths
