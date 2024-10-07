# -*- coding: utf-8 -*-
# @Time    : 2023/2/25 19:13
# @Author  : MyNextWeekend
import pyautogui

# 屏幕的像素
size = pyautogui.size()
# 鼠标所在的位置
pyautogui.position()
# （x，y）坐标是否在屏幕中 Ture / False
pyautogui.onScreen(100, 100)
# 鼠标在时间内移动到指定的坐标
pyautogui.moveTo(300, 300, 1)
# 鼠标在时间内移动到当前坐标的相对坐标
pyautogui.moveRel(300, 300, 1)
# 在指定位置点击右键
pyautogui.click(200, 400, button='right')
# print(a)
