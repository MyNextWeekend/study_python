from flask import Flask
import gevent
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()

app = Flask(__name__)
pool = Pool()  # 协程池


def async_callback(arg1, arg2):
    # 模拟异步回调逻辑，这里使用 gevent.sleep() 来模拟耗时操作
    gevent.sleep(5)
    result = f"Callback complete with args: {arg1}, {arg2}"
    print(result)


@app.route('/callback')
def callback():
    # 处理回调请求
    arg1 = "foo"
    arg2 = "bar"

    # 将异步回调逻辑放入协程中执行
    pool.spawn(async_callback, arg1, arg2)

    return 'Callback request accepted'


if __name__ == '__main__':
    app.run(debug=True)
