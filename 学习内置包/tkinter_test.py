# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 22:42
# @Author  : hejinhu
import tkinter

window = tkinter.Tk()
window.title('我的界面')
window.geometry('500x500+400+200')
window.resizable(width=True, height=True)


def my_lable():
    l = tkinter.Label(window, text='微粒贷电催造数', width=20, height=2)
    l.pack()


def my_button():
    b = tkinter.Button(window, text='运行', bg='yellow', width=5, height=2, command=aaa_bbb)
    b.grid(row=2, column=2,)


v1 = tkinter.StringVar()
v1.set('wowowowo')


def aaa_bbb():
    a = v1.get().strip()
    print(a)


def my_entry():
    e = tkinter.Entry(window, textvariable=v1)
    # e.grid(row=0, column=1)
    e.pack()


my_lable()
my_entry()
my_button()
window.mainloop()
