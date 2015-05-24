# coding=utf-8


class BaseExtractor(object):

    def extract(self, response):
        raise NotImplementedError
