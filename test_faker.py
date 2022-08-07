import random

import pymysql
from faker import Faker

f = Faker('zh_cn')

conn = pymysql.connect(host='106.55.186.222', port=3306, user='root', password='1q2w3e4r', database='study',
                       charset='utf8')
cursor = conn.cursor()
aa = []
for i in range(1000):
    name = f.name()
    password = f.numerify()
    address = f.address()
    age = random.randint(10,80)
    birthday = f.date()
    six = random.choice(['男', '女'])
    aa.append((name, password, address, age, birthday, six))

# print(aa)
cursor.executemany(f"INSERT INTO study.people(name, password, address, age, birthday, six)VALUES(%s,%s,%s,%s,%s,%s);",
                   aa)
conn.commit()
conn.close()