# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 23:08
# @Author  : hejinhu
import uiautomator2 as u2

device = u2.connect()

print(device.device_info)

device(text='微信').click()