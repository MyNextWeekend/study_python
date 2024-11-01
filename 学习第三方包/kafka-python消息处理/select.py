from kafka import KafkaConsumer, TopicPartition

bootstrap_server = '127.0.0.1:9092'

# 初始化 KafkaConsumer
consumer = KafkaConsumer(
    bootstrap_servers=[bootstrap_server], # Kafka 服务器地址
    group_id="your_group003",            # 必须指定 group_id
)
# 定义主题名称
topic = 'test_topic001'

# 获取分区列表
partitions = consumer.partitions_for_topic(topic)
if partitions:
    tp_list = [TopicPartition(topic, p) for p in partitions]
    consumer.assign(tp_list)

    total_uncommitted_messages = 0

    # 遍历每个分区并计算未消费的消息数量
    for tp in tp_list:
        # 获取最新的位点（log end offset）
        end_offset = consumer.end_offsets([tp])[tp]
        # 获取当前消费者组的已提交位点（committed offset）
        committed_offset = consumer.committed(tp) or 0  # 如果没有已提交的位点则为 0

        # 计算未消费的消息数量
        uncommitted_messages = end_offset - committed_offset
        total_uncommitted_messages += max(uncommitted_messages, 0)  # 确保不为负值

        print(f"Partition: {tp.partition}, Committed Offset: {committed_offset}, End Offset: {end_offset}, Uncommitted Messages: {uncommitted_messages}")

    print(f"Total uncommitted messages in topic '{topic}': {total_uncommitted_messages}")
else:
    print(f"No partitions found for topic '{topic}'")
