# coding=utf-8


def reload_encoding(encode):
    import sys
    reload(sys)
    sys.setdefaultencoding(encode)
