import pandas as pd

data_json = {
    "班级": ["一班", "一班", "一班", "一班", "二班", "二班", "二班", "二班"],
    "姓名": ["张三", "张三", "李四", "李四", "张三", "张三", "李四", "李四"],
    "分数": [100, 90, 80, 70, 60, 50, 40, 30],
    "年龄": [20, 23, 26, 29, 32, 35, 38, 41]
}

writer = pd.ExcelWriter("./result.xlsx", engine="openpyxl")
start_row = 3
for i in range(10):
    data = pd.DataFrame(data_json)
    # 指定写入sheet名称以及起始行，丢弃行索引
    data.to_excel(writer, sheet_name="hello", startrow=start_row, index=False)
    start_row = start_row + data.shape[0] + 5  # 标题占1行，空4行

writer.close()
