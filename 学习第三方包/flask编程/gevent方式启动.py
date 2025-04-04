import time
from multiprocessing import Process

from flask import Flask
from gevent import monkey
from gevent.pool import Pool
from gevent.pywsgi import WSGIServer

monkey.patch_all()

app = Flask(__name__)
pool = Pool()  # 协程池


def async_callback(arg1, arg2):
    # 模拟异步回调逻辑，这里使用 gevent.sleep() 来模拟耗时操作
    time.sleep(5)
    result = f"Callback complete with args: {arg1}, {arg2}"
    print(result)


@app.route("/callback")
def callback():
    # 处理回调请求
    arg1 = "foo"
    arg2 = "bar"

    # 将异步回调逻辑放入协程中执行
    pool.spawn(async_callback, arg1, arg2)

    return "Callback request accepted"


if __name__ == "__main__":
    # app.run(debug=True)
    # 启动 一个进程+协程 处理
    # server = WSGIServer(("0.0.0.0", 8000), app)
    # server.serve_forever()

    # 方式二：启动 多个进程+协程 处理
    server = WSGIServer(("0.0.0.0", 8000), app)
    server.start()

    def server_forever():
        server.start_accepting()
        server.stop_event.wait()

    for _ in range(3):  # 此处代表启动多个进程任务
        p = Process(target=server_forever)
        p.start()
