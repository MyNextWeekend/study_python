# -*- coding: utf-8 -*-
from locust.contrib.fasthttp import FastHttpUser
from locust import task, constant, LoadTestShape, events
import logging


@events.init_command_line_parser.add_listener
def _(parser):  # 设置自定义参数
    parser.add_argument("--organize", type=str, env_var="LOCUST_MY_ARGUMENT", default="商户A", help="针对特定场景")


@events.test_start.add_listener
def _(environment, **kw):  # 全局初始化一些东西的时候使用
    my_arg = environment.parsed_options.organize
    print(f"接收到参数:{my_arg}")


class MyUserBe(FastHttpUser):  # 内置两种（FastHttpUser、HttpUser）
    host = r"https://www.baidu.com"  # 设置网站根地址

    # constant(10)：常数（等待时间）
    # between(1, 5)：执行后等待 1 到 5 秒
    # constant_pacing(10)：任务将始终每 10 秒执行一次，如果一个任务执行超过了指定的wait_time，那么在开始下一个任务之前wait将为0。
    wait_time = constant(3)

    @task
    def my_task1(self):
        print(f"my_argument={self.environment.parsed_options.organize}")  # 每个用户直接使用

        # /hello 会自动拼接host地址组装实际请求地址
        with self.client.get("/hello", catch_response=True, name="hello") as res:  # catch_response=true 可以自定义成功与失败
            # {'request_type': 'GET', 'name': 'hello', 'context': {}, 'exception': None,
            # 'response': <locust.contrib.fasthttp.FastResponse object at 0x107584160>,
            # 'response_length': 203, 'response_time': 74}
            logging.info(f"可以用于记录日志信息:{res.request_meta}")

            if res.status_code != 200:
                logging.info("code err")
                res.failure("code err")  # 将响应结果置为失败并设置失败原因
                return
            if res.text == "":  # 根据接口响应类型采用res.text或者res.json() 用于断言响应结果
                logging.info("empty body")
                res.failure("empty body")  # 将响应结果置为失败并设置失败原因
                return

            res.success()  # 将响应结果置为成功

    def on_start(self):
        """用户启动的时候执行"""
        logging.info("start")

    def on_stop(self):
        """用户停止的时候执行"""
        logging.info("on_stop")


class StagesShp(LoadTestShape):
    """负载配置"""
    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None


if __name__ == '__main__':
    import os

    os.system(" locust -f locust_test.py")
    # os.system(" locust -f locust_test.py --master")
