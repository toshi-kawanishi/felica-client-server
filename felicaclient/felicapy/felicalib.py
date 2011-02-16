#!/usr/bin/env python
# -*- coding:utf-8 -*-
from ctypes import *


class StrPasori(Structure):
    pass


class Felica(Structure):
    MAX_SYSTEM_CODE = 8
    MAX_AREA_CODE = 16
    MAX_SERVICE_CODE = 256

    _fields_ = [('p', POINTER(StrPasori)),
                ('systemcode', c_ushort),
                ('IDm', c_ubyte * 8),
                ('PMm', c_ubyte * 8),
                ('num_system_code', c_ubyte),
                ('system_code', c_ushort * MAX_SYSTEM_CODE),
                ('num_area_code', c_ubyte),
                ('area_code', c_ushort * MAX_AREA_CODE),
                ('end_service_code', c_ushort * MAX_AREA_CODE),
                ('num_service_code', c_ubyte),
                ('service_code', c_ushort * MAX_SERVICE_CODE)]


class FelicaLib(object):

    POLLING_ANY = 0xffff
    POLLING_EDY = 0xfe00
    POLLING_SUICA = 0x0003

    def __init__(self):
        self.flib = cdll.felicalib

    def pasori_open(self, dummy):
        ''' PaSoRi をオープンする
        '''
        self.flib.pasori_open.restype = POINTER(StrPasori)

        return self.flib.pasori_open()

    def pasori_close(self, p):
        ''' PaSoRi ハンドルをクローズする
        '''
        self.flib.pasori_close(p)

    def pasori_init(self, p):
        ''' PaSoRi を初期化する
        '''
        return self.flib.pasori_init(p)

    def felica_polling(self, p, systemcode, rfu, timeslot):
        ''' FeliCa をポーリングする
        '''
        self.flib.felica_polling.restype = POINTER(Felica)

        return self.flib.felica_polling(p, systemcode, rfu, timeslot)

    def felica_free(f):
        ''' felica ハンドル解放
        '''
        self.flib.felica_free(f)

    def felica_getidm(self, f, buf):
        ''' IDm 取得
        '''
        self.flib.felica_getidm(f, buf)

    def felica_getpmm(self, f, buf):
        ''' PMm 取得
        '''
        self.flib.felica_getpmm(f, buf)

    def felica_read_without_encryption02(self, f, servicecode, mode, addr,
                                         data):
        ''' 暗号化されていないブロックを読み込む
        '''
        return self.flib.felica_read_without_encryption02(f, servicecode,
                                                          mode, addr, data)

    def felica_write_without_encryption(self, f, servicecode, addr, data):
        ''' 暗号化されていないブロックを書き込む
        '''
        return self.flib.felica_write_without_encryption(f, servicecode,
                                                         addr, data)

    def felica_enum_systemcode(self, p):
        ''' システムコードの列挙
        '''
        self.flib.felica_enum_systemcode.restype = POINTER(Felica)

        return self.flib.felica_enum_systemcode(p)

    def felica_enum_service(self, p, systemcode):
        ''' サービス/エリアコードの列挙
        '''
        self.flib.felica_enum_service.restype = POINTER(Felica)

        return self.flib.felica_enum_service(p, systemcode)
