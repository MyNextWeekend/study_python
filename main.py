class abc:
    age = ''

    def __init__(self):
        self.name = ''

    def set_name(self, name):
        if len(name) > 3 or len(name) < 2:
            print('输入的名字不合法')
        else:
            self.name = name

    @classmethod
    def get_age(cls):
        return cls.age


if __name__ == '__main__':
    abc.age = 99  # 类属性赋值
    obj = abc()  # 实例对象
    print(abc.get_age())  # 99
    print(obj.get_age())  # 99
    print('-------')
    # obj.age = 1999
    print(abc.get_age())  # 99
    print(obj.get_age())  # 99
    print(obj.age)  # 1999
