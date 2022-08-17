import random
from test_lambda import outter


def hanoi(n, a, b, c):
    """汗罗塔"""
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('step  moving from %s to %s' % (a, c))
        # step = 1 + step
        hanoi(n - 1, b, a, c)


@outter
def maopao(list):
    """冒泡排序"""
    for i in range(1, len(list)):
        for j in range(0, len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


if __name__ == '__main__':
    # hanoi(3, 'A', 'B', 'C')

    # list = [random.randint(2000, 3000) for i in range(6)]
    # print(list)
    # print('最大值：%i' % max(list))
    # print('最小值：%i' % min(list))

    # print(maopao(list)
    maopao(list)
    print(list)
