from tkinter import *
from tkinter.messagebox import *


class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.create_page()

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text="药品名称: ").grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        Label(self, text="进价 /元: ").grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E)
        Label(self, text="售价 /元: ").grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)
        Label(self, text="优惠 /元: ").grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)
        Button(self, text="录入").grid(row=6, column=1, stick=E, pady=10)


class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.create_page()

    def create_page(self):
        Label(self, text="查询界面").pack()


class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_page()

    def create_page(self):
        Label(self, text="统计界面").pack()


class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_page()

    def create_page(self):
        Label(self, text="关于界面").pack()


class MainPage:
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("%dx%d" % (600, 400))  # 设置窗口大小
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.create_page()

    def create_page(self):
        self.inputPage.pack()
        menubar = Menu(self.root)
        menubar.add_command(label="数据录入", command=self.input_data)
        menubar.add_command(label="查询", command=self.query_data)
        menubar.add_command(label="统计", command=self.count_data)
        menubar.add_command(label="关于", command=self.about_disp)
        self.root["menu"] = menubar  # 设置菜单栏
        self.count_data()  # 默认显示数据录入界面

    def input_data(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def query_data(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def count_data(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def about_disp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()


class LoginPage:
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("%dx%d" % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text="账111户: ").grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text="密码: ").grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show="*").grid(
            row=2, column=1, stick=E
        )
        Button(self.page, text="登陆", command=self.login_check).grid(
            row=3, stick=W, pady=10
        )
        Button(self.page, text="退出", command=self.page.quit).grid(
            row=3, column=1, stick=E
        )

    def login_check(self):
        name = self.username.get()
        secret = self.password.get()
        if name == "admin" and secret == "123456":
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title="错误", message="账号或密码错误！")


if __name__ == "__main__":
    root = Tk()
    root.title("小程序")
    root.geometry("500x500+500+200")
    LoginPage(root)
    root.mainloop()
