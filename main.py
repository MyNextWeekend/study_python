import json
import time

import requests


def get_history_data():
    '''
    获取历史数据
    :return:历史数据
    '''
    # 接口地址
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    # 请求的时候带上请求头，模拟浏览器发送请求
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    res = requests.get(url, headers).json()
    data_all = json.loads(res.get('data'))

    history_data = {}
    # 每天的总人数
    for chinaDayList_item in data_all.get("chinaDayList"):
        date = '2022.' + chinaDayList_item['date']
        date = time.strftime('%Y-%m-%d', time.strptime(date, '%Y.%m.%d'))  # 将2020.04.21的时间格式转换成2020-04-21，方便插入到数据库中
        confirm_num = chinaDayList_item['confirm']  # 获取确诊人数
        suspect_num = chinaDayList_item['suspect']  # 获取疑似人数
        dead_num = chinaDayList_item['dead']  # 获取死亡人数
        heal_num = chinaDayList_item['heal']  # 获取治愈人数
        history_data[date] = {'confirm_num': confirm_num, 'suspect_num': suspect_num, 'dead_num': dead_num,
                              'heal_num': heal_num}
    # 每天新增人数
    for chinaDayAddList_item in data_all['chinaDayAddList']:
        # print(chinaDayAddList_item)
        date = '2022.' + chinaDayAddList_item['date']
        # print(type(date), date)  # <class 'str'> 2020.04.21
        date = time.strftime('%Y-%m-%d', time.strptime(date, '%Y.%m.%d'))  # 将2020.04.21的时间格式转换成2020-04-21，方便插入到数据库中
        # print(date)
        confirm_add_num = chinaDayAddList_item['confirm']  # 获取新增确诊人数
        # print(confirm_num)
        suspect_add_num = chinaDayAddList_item['suspect']  # 获取新增疑似人数
        dead_add_num = chinaDayAddList_item['dead']  # 获取新增死亡人数
        heal_add_num = chinaDayAddList_item['heal']  # 获取新增治愈人数
        history_data[date].update(
            {'confirm_add_num': confirm_add_num, 'suspect_add_num': suspect_add_num, 'dead_add_num': dead_add_num,
             'heal_add_num': heal_add_num})
    return history_data


print(get_history_data())
