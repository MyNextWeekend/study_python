import os
from atexit import register


def main():
    print('main')


def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))


# register(goodbye, 'Donny', 'nice')
# or:
# register(goodbye, adjective='nice', name='Donny')
if __name__ == '__main__':
    register(goodbye, adjective='nice', name='Donny')
    main()
    exit(1)  # 程序退出了
    print("chegn xu")
