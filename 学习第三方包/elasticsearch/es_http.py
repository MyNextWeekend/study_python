import requests


def query_all_index():
    url = "http://106.55.186.222:9200/_cat/indices"
    res = requests.get(url=url)
    print(res.text)


def es_health():
    url = "http://106.55.186.222:9200/_cluster/health"
    res = requests.get(url=url)
    print(res.text)


if __name__ == '__main__':
    query_all_index()
    es_health()
