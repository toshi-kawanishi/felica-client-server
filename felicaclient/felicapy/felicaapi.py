#!/usr/bin/env python
# -*- coding:utf-8 -*-
from ctypes import *
from felicalib import FelicaLib


class FelicaPy(object):

    def __init__(self, f):
        self.f = f

    def getidm(self):
        idm_array = ['%02X' % x for x in self.f.contents.IDm]
        idm_array.reverse()

        return ''.join(idm_array)


class FelicaApi(object):

    def __init__(self):
        self.lib = FelicaLib()
        self.p = self.lib.pasori_open(None)
        self.lib.pasori_init(self.p)

    def __del__(self):
        self.lib.pasori_close(self.p)

    def polling_any(self):
        f = self.lib.felica_polling(self.p, self.lib.POLLING_ANY, 0, 0)

        return FelicaPy(f)

    def polling_edy(self):
        f = self.lib.felica_polling(self.p, self.lib.POLLING_EDY, 0, 0)

        return FelicaPy(f)

    def polling_suica(self):
        f = self.lib.felica_polling(self.p, self.lib.POLLING_SUICA, 0, 0)

        return FelicaPy(f)
