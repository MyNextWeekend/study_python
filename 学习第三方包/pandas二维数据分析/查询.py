# -*- coding: utf-8 -*-
# @Time    : 2023/7/15 14:18
# @Author  : hejinhu
import pandas as pd

data_json = {
    "班级": ["一班", "一班", "一班", "一班", "二班", "二班", "二班", "二班"],
    "姓名": ["张三", "张三", "李四", "李四", "张三", "张三", "李四", "李四"],
    "分数": [100, 90, 80, 70, 60, 50, 40, 30],
    "年龄": [20, 23, 26, 29, 32, 35, 38, 41]
}

if __name__ == '__main__':
    df = pd.DataFrame(data_json)
    # print(df)
    # 查询符合条件，并按照分数排序
    df = df.query("姓名=='张三'").sort_values("分数")
    for row in df.itertuples(index=False):
        print(row.班级, row.姓名, row.分数, row.年龄)
