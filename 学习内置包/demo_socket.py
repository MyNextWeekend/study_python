import socket
import threading
import time


class SendMessage(threading.Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s

    def run(self):
        while True:
            print("-" * 20)
            msg = input("请输入需要发送的消息：")
            self.s.sendto(msg.encode("UTF-8"), ("", 55666))
            time.sleep(1)


class RecvMessage(threading.Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s

    def run(self):
        while True:
            msg = self.s.recvfrom(1024)
            print(f'接收的消息：{msg[0].decode("UTF-8")}')
            print(f"对方的IP地址：{msg[1]}")
            time.sleep(2)


def main():
    HOST = ""
    s = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM
    )  # 定义socket类型，网络通信，TCP
    s.bind((HOST, 55666))  # 套接字绑定的IP与端口
    r_list = []
    for i in range(2):
        r = RecvMessage(s)
        r.start()
        r_list.append(r)
    for i in r_list:
        i.join()

    s = SendMessage(s)
    s.start()
    s.join()


if __name__ == "__main__":
    main()
