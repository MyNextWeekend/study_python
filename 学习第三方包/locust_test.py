# -*- coding: utf-8 -*-
# @Time    : 2022/10/30 21:50
# @Author  : hejinhu
import os

from locust.contrib.fasthttp import FastHttpUser
from locust import task, constant


class MyUserBe(FastHttpUser):
    wait_time = constant(10)

    @task
    def demo(self):
        pass

    # @task
    # def my_task1(self):
    #     with self.client.get("https://www.baidu.com/", catch_response=True) as res:
    #         if res.status_code == 200:
    #             print("成功")
    #         else:
    #             print("失败")


if __name__ == '__main__':
    # os.system(" locust -f main.py")
    os.system(" locust -f main.py --master")
