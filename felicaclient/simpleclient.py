#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
_script_directry = os.path.dirname(os.path.abspath(__file__))
from felicapy.felicaapi import FelicaApi
import time


class SimpleFelicaClient(object):

    def run(self, call_method, args=(), kwargs={}, timeout=10):
        api = FelicaApi()
        count = 0
        while(count < timeout):
            try:
                felica = api.polling_any()
                call_method(felica, *args, **kwargs)
            except Exception:
                print 'error'

            time.sleep(1)
            count += 1

