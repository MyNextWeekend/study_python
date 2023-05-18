import time

from elasticsearch import Elasticsearch


def insert():
    # -- create 方法 创建一条对应索引,文档类型,指定id的一条数据
    es.create(index='world', doc_type='country', id=0, body={'name': '中国', 'region': '亚洲'})
    es.create(index='world', doc_type='country', id=1, body={'name': '日本', 'region': '亚洲'})
    # -- index 方法 插入一条对应索引，文档类型的数据, id可以指定也可以由其自动生成
    es.index(index='world', doc_type='country', id=2, body={'name': '韩国', 'region': '亚洲'})
    es.index(index='world', doc_type='country', body={'name': '印度', 'region': '亚洲'})
    es.index(index='world', doc_type='country', body={'name': '中国人', 'region': '亚洲'})


def query():
    world1 = es.search(index='world', doc_type='country')
    print(world1)


def delete():
    if es.indices.exists(index="world"):  # 查询索引是否存在
        es.indices.delete(index="world")  # 删除索引
        print("索引删除成功")
    else:
        print("索引不存在")


if __name__ == '__main__':
    es = Elasticsearch([{"host": "106.55.186.222", "port": 9200}], timeout=3600)
    print(es.ping())
    # insert()
    query()
    # time.sleep(1)
    # delete()
