#coding=utf-8

from ..libs import links
import re
import json
from ..libs import priority
from b2 import exceptions2

__all__ = ["BaseFilter", "SiteFilter", "UrlRegxFilter", "UrlDirPathFilter"]


class BaseFilter(object):
    """基础过滤器基类
    """

    def __init__(self,
                 filter_name,
                 must_check=False,
                 priority=priority.FILTER_PRIORITY.NONE,
                 ignore=False):
        self.filter_name = filter_name
        self._must_check = must_check
        self._priority = priority
        self._ignore = ignore

    def filter(self, url):
        """url match relu
            param:url:page:请求的页面
            return:filter:boolean:如果被过滤掉返回True,否则返回False
        """
        return False

    def set_must_check(self):
        self._must_check = True

    def must_check(self):
        return self._must_check

    def priority(self):
        return self._priority

    def __str__(self):
        return json.dumps({"filterName": self.filter_name})

    def get_url(self, url):
        if url and isinstance(url, dict) and "url" in url:
            url = url["url"]
        elif url and hasattr(url, "url"):
            url = getattr(url, "url")
        elif (url and isinstance(url, basestring)) is False:
            raise ValueError
        return url

    def update(self, *argv, **kw):
        pass

    def ignore(self):
        return self._ignore


class SiteFilter(BaseFilter):
    """根据站点过滤
        >>> sitefilter = SiteFilter()
    """

    def __init__(self, sites):
        super(SiteFilter, self).__init__(
            "site_filter",
            must_check=True,
            priority=priority.FILTER_PRIORITY.VERY_HIGH)
        self.sites = set()
        self._add_site(sites)

    def _add_site(self, site):
        exceptions2.judge_null(site)
        if isinstance(site, basestring):
            self.sites.add(site)
        elif isinstance(site, (list, tuple, set)):
            self.sites.update(site)
        else:
            raise ValueError

    def filter(self, url):
        url = self.get_url(url)
        url_site = links.get_url_site(url)
        if url_site in self.sites:
            return False
        return True

    def update(self, *argv, **kw):
        site = kw.get("site", None)
        if site and isinstance(site, basestring):
            self.sites.add(site)
            return (True, None)
        return (False, "unsupport type your input")


class UrlRegxFilter(BaseFilter):
    """链接正则过滤类
        test:
            >>> url_filter = UrlRegxFilter("test.com/xxx[0-9]*")
            >>> url_filter.filter("test.com/xxx3")
            >>> url_filter.filter("test.com/xx4")
    """

    def __init__(self, url_regxs):
        super(UrlRegxFilter, self).__init__("url_regx")
        if url_regxs and isinstance(url_regxs, basestring):
            self.url_patterns = [re.compile(url_regxs)]
        elif url_regxs and isinstance(url_regxs, (list, tuple)):
            self.url_patterns = [
                re.compile(url_regx) for url_regx in url_regxs
            ]
        else:
            raise ValueError

    def filter(self, url):
        if url and isinstance(url, dict) and "url" in url:
            url = url["url"]
        elif url and hasattr(url, "url"):
            url = getattr(url, "url")
        elif (url and isinstance(url, basestring)) is False:
            raise ValueError
        for pattern in self.url_patterns:
            if pattern.search(url):
                return False
        return True


class UrlStartFilter(BaseFilter):
    """链接开始过滤类
        Test:
            >>> url_filter = UrlStartFilter("http://githuber.cn/people/")
            >>> url_filter.filter("http://githuber.cn/people/2503423")
    """

    def __init__(self, prefix, lower=True):
        super(UrlStartFilter, self).__init__("url_start")
        self.lower = lower
        self.prefix = prefix.lower() if self.lower else prefix

    def filter(self, url):
        if url and isinstance(url, dict) and "url" in url:
            url = url["url"]
        elif url and hasattr(url, "url"):
            url = getattr(url, "url")
        elif (url and isinstance(url, basestring)) is False:
            raise ValueError
        return not url.lower().startswith(
            self.prefix) if self.lower else not url.startswith(self.prefix)

    def __str__(self):
        return json.dumps({
            "filterName": self.filter_name,
            "pattern": self.prefix
        })


class UrlEndFilter(BaseFilter):
    """链接开始过滤类
    """

    def __init__(self, suffix, lower=True):
        super(UrlEndFilter, self).__init__("url_end")
        self.lower = lower
        self.suffix = suffix.lower() if self.lower else suffix
        self.suffix = suffix

    def filter(self, url):
        """如果url链接不符合后缀,则返回过滤状态
        """
        if url and isinstance(url, dict) and "url" in url:
            url = url["url"]
        elif url and hasattr(url, "url"):
            url = getattr(url, "url")
        elif (url and isinstance(url, basestring)) is False:
            raise ValueError
        return not url.lower().endswith(
            self.suffix) if self.lower else not url.endswith(self.suffix)


class UrlDirPathFilter(BaseFilter):
    """根据请求request属性dir_path限制抓取深度
    """

    def __init__(self, dir_path_limit=None):
        super(UrlDirPathFilter, self).__init__(
            "url_dirpath_filter",
            must_check=True,
            priority=priority.FILTER_PRIORITY.VERY_HIGH)
        if dir_path_limit is not None and isinstance(
                dir_path_limit, (int, long)) and dir_path_limit >= 0:
            self.dir_path_limit = dir_path_limit
        else:
            raise TypeError

    def filter(self, request):
        if request is None:
            raise ValueError
        if isinstance(request, dict):
            _dir_path = request.get("dir_path", None)
            if _dir_path is None:
                raise Exception, "%s is not set dirpath" % request
            if _dir_path > self.dir_path_limit:
                return True
            return False
        raise TypeError


class UrlFilterContainer(BaseFilter):
    """根据请求request，如果满足所有过滤条件，才能被保留
    """

    def __init__(self, filters):
        super(UrlFilterContainer, self).__init__("urlfiltercontainer")
        if isinstance(filters, BaseFilter):
            self._filters = [filters]
        else:
            self._filters = filters

    def filter(self, request):
        for _filter in self._filters:
            if _filter.filter(request):
                return True
        return False
