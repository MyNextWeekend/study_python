import pandas as pd

df = pd.read_excel('./out_put.xlsx', sheet_name=0)
print(df)
# df["成绩"] = [66, 77, 88, 99]
# df.loc['5'] = ["张三", 2, 3]
# df["综合"] = df['age'] + df['成绩']
# print(df)
# df.to_excel('./out_put.xlsx')
