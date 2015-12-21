#coding=utf-8





from xspider.fetch.fetcher import BaseRequestsFetcher
from xspider.model.models import ZRequest


if __name__ == "__main__":
    fetch = BaseRequestsFetcher()
    request = ZRequest("http://www.126.com")
    for i in fetch.fetch(request):
        print i 
