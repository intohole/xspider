# coding=utf-8


class BaseSaver(object):

    def save(self, *argv, **kw):
        raise NotImplementedError
