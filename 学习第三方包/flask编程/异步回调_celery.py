# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 11:13
# @Author  : hejinhu
from flask import Flask
from celery import Celery

app = Flask(__name__)

# 配置 Celery
app.config['CELERY_BROKER_URL'] = 'amqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://guest@localhost//'

# 创建 Celery 实例
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def async_callback(arg1, arg2):
    # 模拟异步回调逻辑，这里使用 time.sleep() 来模拟耗时操作
    import time
    time.sleep(5)
    result = f"Callback complete with args: {arg1}, {arg2}"
    print(result)


@app.route('/callback')
def callback():
    # 处理回调请求
    arg1 = "foo"
    arg2 = "bar"

    # 调用异步任务
    async_callback.delay(arg1, arg2)

    return 'Callback request accepted'


if __name__ == '__main__':
    app.run(debug=True)
"""
另一个终端窗口中运行以下命令来启动 Celery worker：
celery -A your_app_name worker --loglevel=info
"""