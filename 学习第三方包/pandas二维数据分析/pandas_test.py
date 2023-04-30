import pandas as pd
import requests

data_json = {
    "班级": ["一班", "一班", "一班", "一班", "二班", "二班", "二班", "二班"],
    "姓名": ["张三", "张三", "李四", "李四", "张三", "张三", "李四", "李四"],
    "分数": [100, 90, 80, 70, 60, 50, 40, 30],
    "年龄": [20, 23, 26, 29, 32, 35, 38, 41]
}
df = pd.DataFrame(data_json)
df = df.groupby(["班级", "姓名"], as_index=False).agg({"分数": "sum", "年龄": "min"})
new_df = pd.DataFrame()
for name, group in df.groupby("班级"):
    group.loc[f"{name}合计"] = group[["分数", "年龄"]].sum()
    new_df = pd.concat([new_df, group[-1:], group[:-1]])

new_df.loc["总合计"] = df[["分数", "年龄"]].sum()
new_df = pd.concat([new_df[-1:], new_df[:-1]])
# new_df['班级'] = new_df['班级'].fillna(new_df.index.to_series())
new_df['姓名'] = new_df['姓名'].fillna(new_df.index.to_series())
new_df = new_df.set_index(["班级", "姓名"])
print(new_df)
# new_df.to_excel("./a.xlsx")

