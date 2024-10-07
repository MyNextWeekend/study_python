import redis

client = redis.Redis(host='106.55.186.222', port=6379, password="asdfgqwet123df12345", db=1, decode_responses=True)
client.set('name', '张三', px=30000)  # 设置 name 对应的值 px过期时间 毫秒
client.set('age', 18)  # 设置 name 对应的值

print(client['age'])
print(client.get('name'))  # 取出键 name 对应的值
print(type(client.get('age')))  # 查看类型
