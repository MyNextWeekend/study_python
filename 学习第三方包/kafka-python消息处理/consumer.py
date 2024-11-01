from kafka import KafkaConsumer, TopicPartition

bootstrap_server = '127.0.0.1:9092'
topic = 'test_topic001'
group_id = 'your_group003'


def get_one():
    consumer = KafkaConsumer(
        topic,
        group_id=group_id,
        bootstrap_servers=[bootstrap_server],
        auto_offset_reset='latest',
        enable_auto_commit=False  # 禁用自动提交
    )

    for message in consumer:
        print(f"Offset: {message.offset}, Message: {message.value}")

        # 手动提交消费位点
        consumer.commit()


def get_many():
    # 初始化 KafkaConsumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[bootstrap_server],
        group_id=group_id,
        auto_offset_reset='latest',
        enable_auto_commit=True,  # 自动提交偏移量
        max_poll_records=1000  # 每次拉取最多 1000 条消息
    )

    # 拉取消息
    messages = consumer.poll(timeout_ms=1000)  # 设置超时，防止无消息时阻塞

    # 遍历并处理消息
    for tp, msgs in messages.items():
        for msg in msgs:
            print(f"{tp} Consumed message at offset {msg.offset}: {msg.value}")

    consumer.close()


if __name__ == '__main__':
    get_many()
