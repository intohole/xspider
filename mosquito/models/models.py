# coding=utf-8


class Urls(object):

    __slots__ = ('url')

    def __init__(self, url):
        self.url = url


class Response(object):

    __slots__ = ('body', 'url', 'status')

    def __init__(self, url, status, body=''):
        self.url = url
        self.status = status
        self.body = body
