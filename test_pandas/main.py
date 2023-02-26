import pandas as pd
import requests


def get_data():
    headers = {}
    body = {}
    result = requests.post("", headers=headers, json=body)
    if result.status_code != 200:
        raise Exception(f"返回code异常：{result.status_code}")
    return result.json()


def writer_excel(df: pd.DataFrame):
    df.fillna({"分数": 0})  # 空值填充0
    df = df.groupby("zu").agg({"分数": "sum", "科目": "count"})

    with pd.ExcelWriter("./res.xlsx") as writer:
        df.to_excel(writer, sheet_name="第一页")


if __name__ == '__main__':
    res = get_data()
