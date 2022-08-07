def aa():
    for i in range(5):
        yield i


if __name__ == '__main__':
    a = aa()
    print(a)