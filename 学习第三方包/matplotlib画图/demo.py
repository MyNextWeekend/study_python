import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("MacOSX")  # macOS 可用 'MacOSX'，Linux/Windows 用 'TkAgg'
# 使用支持中文的字体（macOS 自带 “Heiti” 或 “PingFang”）
matplotlib.rcParams["font.sans-serif"] = ["Heiti TC", "PingFang SC", "Arial Unicode MS"]
matplotlib.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 数据
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 18, 16]
y2 = [8, 12, 11, 14, 10]

plt.plot(x, y1, marker="o", label="产品A")
plt.plot(x, y2, marker="s", label="产品B")

# 添加标题和标签
plt.title('多折线图示例')
plt.xlabel('时间')
plt.ylabel('数值')

plt.legend()

# 显示网格
plt.grid(True)
# 显示图形
plt.show()
