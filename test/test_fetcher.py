from mosquito.downloader.fetcher import BaseFetcher

if __name__ == '__main__':
    a = BaseFetcher()
    for i in a.request('http://www.baidu.com'):
        print i.encoding
        print i.text
