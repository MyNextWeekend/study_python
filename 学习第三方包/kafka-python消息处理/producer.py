# -*- coding: utf-8 -*-

import json,time
from kafka import KafkaProducer
from kafka.errors import KafkaError

bootstrap_server = '127.0.0.1:9092'


def kfk_produce_2():
    """
        发送 string 格式数据
    :return:
    """
    producer = KafkaProducer(bootstrap_servers=bootstrap_server)
    data_dict = {
        "name": 'king',
        'age': 100,
        "msg": "Hello World"
    }
    msg = json.dumps(data_dict).encode()
    producer.send('test_topic001', msg, partition=1)
    producer.close()


if __name__ == "__main__":
    for i in range(5):
        start = time.time()
        kfk_produce_2()
        print(f"耗时是:{time.time()-start:.2f}")
