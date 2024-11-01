from kafka import KafkaAdminClient
from kafka import TopicPartition

# Kafka 服务器配置
bootstrap_server = '127.0.0.1:9092'
group_id = 'your_group_id'
topic = 'your_topic'
partition = 0  # 要修改的分区
new_offset = 5  # 新的偏移量

# 初始化 AdminClient
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_server)

# 创建分区对象
tp = TopicPartition(topic, partition)

# 创建新的偏移量
offsets = {tp: new_offset}

# 修改已提交的偏移量
print(admin_client.list_consumer_group_offsets(group_id, partition=0))

# 关闭 AdminClient
admin_client.close()
print("Offset updated successfully")
