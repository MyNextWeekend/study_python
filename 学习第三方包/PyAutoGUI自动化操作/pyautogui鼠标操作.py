# @Time    : 2023/2/25 19:13
# @Author  : MyNextWeekend
# 官网地址 https://pyautogui.readthedocs.io/en/latest/screenshot.html
import time

import pyautogui

# 屏幕的像素
size = pyautogui.size()
print(f"{size=}")
# 鼠标所在的位置
print(f"{pyautogui.position()=}")
# （x，y）坐标是否在屏幕中 Ture / False
pyautogui.onScreen(100, 100)
# 鼠标在时间内移动到指定的坐标
pyautogui.moveTo(300, 300, 1)
# 鼠标在时间内移动到当前坐标的相对坐标
pyautogui.moveRel(300, 300, 1)
# 在指定位置点击右键
pyautogui.click(200, 400, button="right")

# 通过图片找到位置
notion = pyautogui.locateOnScreen("bilibili.png")
print(notion)
notion_point = pyautogui.center(notion)
print(notion_point)
pyautogui.click(notion_point.x, notion_point.y)
time.sleep(2)
pyautogui.doubleClick(notion_point)

# 弹窗交互
pyautogui.alert(text="确定要做什么吗？", title="标题AAAAA")
time.sleep(5)
