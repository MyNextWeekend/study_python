class AgeExceptin(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'输入的年龄【{self.msg}】不符合规范'


def test():
    age = int(input('输入年龄：'))
    if age > 150 or age < 1:
        raise AgeExceptin(age)
    else:
        print('输入的年龄是正确的')


try:
    test()
except AgeExceptin as e:
    print(e)
