# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 09:39
# @Author  : MyNextWeekend
import hashlib
import hmac
import base64


def hmac_sha1(key, msg):
    """返回加密之后aiisic"""
    return hmac.new(key.encode('UTF-8'), msg.encode('UTF-8'), hashlib.sha1).digest()


if __name__ == '__main__':
    key = '123'
    msg = 'msg'
    res = hmac_sha1(key,msg)
    print(base64.b64encode(res))
