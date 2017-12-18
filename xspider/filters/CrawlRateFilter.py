#coding=utf-8

from UrlFilter import BaseFilter
from ..libs import links
from ..libs import priority
import time

__all__ = ["CrawledSiteRateFilter"]


class SiteRateInfo(object):
    def __init__(self, site, time_type, max_count):
        self.site = site
        self.count = 0
        self.time_type = time_type
        self.max_count = 0
        self.time = time.time()

    def dec(self):
        pass

    def isChange(self):
        pass


class TimeRateFilter(BaseFilter):
    def __init__(self, every=1, wait=0.1):
        super(TimeRateFilter, self).__init__(
            "time_rate_filter", priority.FILTER_PRIORITY.HIGHEST, ignore=True)
        self._old = time.time()
        self._every = every
        self._wait = wait
        self._switch = True

    def filter(self, request):
        now = time.time()
        diff = now - self._old
        if diff > self._every and self._switch:
            time.sleep(self._wait)
            self._old = now
            self._switch = False
        self._switch = False
        return False
