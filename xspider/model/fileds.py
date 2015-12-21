#coding=utf-8

import json


class Fileds(dict):

    def __str__(self):
        return json.dumps(self)
