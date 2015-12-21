#coding=utf-8

import json


class Fileds(dict):

    def __str__(self):
        print "fildes"
        return json.dumps(self)
